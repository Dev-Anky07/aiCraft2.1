import glob
def find_unique_classes(annotation_path):
    unique_classes = set()
    for annotation_file in glob.glob(annotation_path):
        with open(annotation_file, 'r') as f:
            lines = f.readlines()
        for line in lines:
            parts = line.strip().split()
            if len(parts) > 0:
                class_id = int(parts[0])
                unique_classes.add(class_id)
    print("Unique class IDs in the dataset:", unique_classes)
    return unique_classes

#testset_annotations = '/Users/anky/Documents/GitHub/aiCraft/set1/train/labels/*.txt'
#testset_annotations = '/Users/anky/Documents/GitHub/aiCraft/set1/valid/labels/*.txt'
dataset2_annotations = '/Users/anky/Documents/GitHub/aiCraft/Dataset2ObjDet/Labels/txt/*.txt'
#find_unique_classes(testset_annotations)
find_unique_classes(dataset2_annotations)