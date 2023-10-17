from django.shortcuts import render
from .forms import ImageForm, Image,DepressionAssessmentForm
# import os
import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# import matplotlib.image as im
# import sys
from keras.models import load_model
import matplotlib.pyplot as plt
import os
# Create your views here.




def home(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    form = ImageForm()
    img = Image.objects.all()

    return render(request, 'disease/home.html', {'img':img,'form':form})

def predict(request):
    import os
    for dirname, _, filenames in os.walk('Dataset'):
        for filename in filenames:
            print(os.path.join(dirname, filename))

    from tensorflow import keras

    height = 200
    width = 200
    channels = 1

    data_dir = 'Dataset'
    # from pathlib import Path
    # dataset_path = Path('/Dataset/')

    dataset = keras.preprocessing.image_dataset_from_directory(
        'Dataset',
        shuffle=True,
        image_size=(200, 200),
        batch_size=(32)
    )

    class_names = dataset.class_names
    class_names



    pic = 'media'
    model = load_model('dementia2.h5')

    dataset1 = keras.preprocessing.image_dataset_from_directory(pic, shuffle=True, image_size=(176, 208), batch_size=1)

    clas = dataset1.class_names

    for image_batch, label_batch in dataset1.take(1):
        first_image = image_batch[0].numpy().astype('uint8')
        first_label = label_batch[0].numpy()

        print("First image to predict")
        plt.imshow(first_image)
        print('actual label:', clas[first_label])

        batch_prediction = model.predict(image_batch)
        print("predicted label:", class_names[np.argmax(batch_prediction)])
        ab = class_names[np.argmax(batch_prediction)]

        print("test end")
        pi = Image.objects.all()
        pi.delete()
        import shutil
        shutil.rmtree('media/myimage')

        return render(request,'disease/pred.html',{'ab':ab})



def depression_assessment(request):
    if request.method == 'POST':
        form = DepressionAssessmentForm(request.POST)
        if form.is_valid():
            score = 0
            for answer in form.cleaned_data.values():
                score += int(answer)

            if score < 5:
                result = "minimal or no depression"
            elif score < 10:
                result = "mild depression"
            elif score < 15:
                result = "moderate depression"
            elif score < 20:
                result = "moderately severe depression"
            else:
                result = "severe depression"

            return render(request, template_name='disease/assessment_result.html', context={'result': result})
    else:
        form = DepressionAssessmentForm()

    return render(request, template_name='disease/assessment.html', context={'form': form})
