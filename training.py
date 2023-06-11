from matminer.featurizers.composition import ElementProperty

featurizer = ElementProperty.from_preset(preset_name="magpie")

composition = "Fe2O3"
features = featurizer.featurize(composition)
print(features)