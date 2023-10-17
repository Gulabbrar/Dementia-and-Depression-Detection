from django import forms
from .models import Image

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = '__all__'
        labels = {'photo':''}


from django import forms


class DepressionAssessmentForm(forms.Form):
    QUESTIONS = [
        ("0", "Not at all"),
        ("1", "Several days"),
        ("2", "More than half the days"),
        ("3", "Nearly every day")
    ]

    question1 = forms.ChoiceField(choices=QUESTIONS, widget=forms.RadioSelect(),
                                  label="Little interest or pleasure in doing things?")
    question2 = forms.ChoiceField(choices=QUESTIONS, widget=forms.RadioSelect(),
                                  label="Feeling down, depressed, or hopeless?")
    question3 = forms.ChoiceField(choices=QUESTIONS, widget=forms.RadioSelect(),
                                  label="Trouble falling or staying asleep, or sleeping too much?")
    question4 = forms.ChoiceField(choices=QUESTIONS, widget=forms.RadioSelect(),
                                  label="Feeling tired or having little energy?")
    question5 = forms.ChoiceField(choices=QUESTIONS, widget=forms.RadioSelect(), label="Poor appetite or overeating?")
    question6 = forms.ChoiceField(choices=QUESTIONS, widget=forms.RadioSelect(),
                                  label="Feeling bad about yourself — or that you are a failure or have let yourself or your family down?")
    question7 = forms.ChoiceField(choices=QUESTIONS, widget=forms.RadioSelect(),
                                  label="Trouble concentrating on things, such as reading the newspaper or watching television?")
    question8 = forms.ChoiceField(choices=QUESTIONS, widget=forms.RadioSelect(),
                                  label="Moving or speaking so slowly that other people could have noticed?")
    question9 = forms.ChoiceField(choices=QUESTIONS, widget=forms.RadioSelect(),
                                  label="Thoughts that you would be better off dead or of hurting yourself in some way?")
