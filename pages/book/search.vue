<template>
  <div>
    <!-- 検索テキストボックス（エンターキーで検索も
    を可能） -->
    <v-row>
      <v-col cols="6">
        <v-text-field
          v-model="keyword"
          label="本のタイトルを検索"
          @keyup.enter="search(keyword)"
        />
      </v-col>
    </v-row>
    <v-row>
      <v-col cols="3">
        <v-btn color="primary" @click="search(keyword)">検索する</v-btn>
      </v-col>
      <v-col cols="3">
        <v-btn color="secondary" to="/book"> 一覧に戻る </v-btn>
      </v-col>
    </v-row>
    <!-- 検索結果がないときに表示 -->
    <div v-show="!isFound" class="mt-4">検索結果は0件でした。</div>
    <!-- 検索結果をイメージ、タイトル、ディスクリプションの３つで一覧表示 -->
    <v-row>
      <v-col
        v-for="(book, index) in searchResults"
        :key="index"
        cols="12"
        md="6"
      >
        <v-card class="mx-auto mb-4">
          <v-row>
            <v-col cols="4">
              <v-img :src="book.image"></v-img>
            </v-col>
            <v-col cols="8">
              <v-card-title>{{ book.title }}</v-card-title>
              {{ book.description }}
              <v-spacer />
              <v-card-actions>
                <v-btn
                  class="mx-2"
                  fab
                  dark
                  color="indigo"
                  @click="addBookList(index)"
                >
                  <v-icon dark> mdi-plus </v-icon>
                </v-btn>
              </v-card-actions>
            </v-col>
          </v-row>
        </v-card>
      </v-col>
    </v-row>
  </div>
</template>

<script>
export default {
  data() {
    return {
      keyword: '',
      searchResults: [],
      isFound: true,
      feature1: null,
    };
  },
  methods: {
    addBookList(index) {
      this.$emit('add-book-list', this.searchResults[index]);
    },
    // keywordをもとにGoogleAPIから本の情報を40件取得する
    async search(keyword) {
      this.searchResults = [];
      // クエリーストリングを作成
      const baseUrl = 'https://www.googleapis.com/books/v1/volumes?';
      const params = {
        q: `intitle:${keyword}`,
        maxResults: 40,
      };
      const queryParams = new URLSearchParams(params);

      // fetchでJSON取得
      const response = await fetch(baseUrl + queryParams).then((response) =>
        response.json()
      );

      if (response.items === undefined) {
        this.isFound = false;
      } else {
        this.isFound = true;
        // 必要な情報をsearchResultsにpush
        for (const book of response.items) {
          const title = book.volumeInfo.title;
          const img = book.volumeInfo.imageLinks;
          const description = book.volumeInfo.description;
          this.searchResults.push({
            title: title || '',
            image: img ? img.thumbnail : '',
            description: description ? description.slice(0, 40) : '',
          });
        }
      }
    },
  },
};
</script>

<style></style>
