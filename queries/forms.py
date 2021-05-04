from django import forms
from django.core.validators import MinValueValidator
from .models import Random, PersonalisedJoke, ChuckFact

PERIODICITY = ( 
	("seconds", "Seconds"),
	("minutes", "Minutes"), 
	("hours", "Hours"),
	("days", "Days")
)

class RandomForm(forms.ModelForm):
	class Meta:
		model = Random
		fields = '__all__'

		widgets={
			'quotes' : forms.CheckboxInput(attrs={'class': 'form-check-input'}),
			'jokes' : forms.CheckboxInput(attrs={'class': 'form-check-input'}),
			'chuckNorris' : forms.CheckboxInput(attrs={'class': 'form-check-input'}),
			'movieReview' : forms.CheckboxInput(attrs={'class': 'form-check-input'}),
			'tweetingTimes' : forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Tweeting times'}),
			'periodicityNumber' : forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Periodicity'}),
			'periodicity' : forms.Select(attrs={'class': 'form-select'})
		}


class PersonalisedJokesForm(forms.ModelForm):
	class Meta:
		model = PersonalisedJoke
		fields = '__all__'

		widgets={
			'categoryAny' : forms.CheckboxInput(attrs={'class': 'form-check-input', 'type':'radio',\
						    'checked':'true', 'id':'categoryAnySwitch', 'onclick':"selectAnyFunc()"}),
			'categoryCustom' : forms.CheckboxInput(attrs={'class': 'form-check-input', 'type':'radio',\
						       'id':'categoryCustomSwitch', 'onclick':"selectCustomFunc()"}),
			'categoryProgramming': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
			'categoryMisc' : forms.CheckboxInput(attrs={'class': 'form-check-input'}),
			'categoryDark' : forms.CheckboxInput(attrs={'class': 'form-check-input'}),
			'categoryPun' : forms.CheckboxInput(attrs={'class': 'form-check-input'}),
			'categorySpooky' : forms.CheckboxInput(attrs={'class': 'form-check-input'}),
			'categoryChristmas' : forms.CheckboxInput(attrs={'class': 'form-check-input'}),
			'flagNsfw' : forms.CheckboxInput(attrs={'class': 'form-check-input'}),
			'flagReligious' : forms.CheckboxInput(attrs={'class': 'form-check-input'}),
			'flagPolitical' : forms.CheckboxInput(attrs={'class': 'form-check-input'}),
			'flagRacist' : forms.CheckboxInput(attrs={'class': 'form-check-input'}),
			'flagSexist' : forms.CheckboxInput(attrs={'class': 'form-check-input'}),
			'flagExplicit' : forms.CheckboxInput(attrs={'class': 'form-check-input'}),
			'searchString' : forms.TextInput(attrs={'class':'form-control', 'type':'text',
	 						 'placeholder':'Keyword'})
		}


class ChuckNorrisWordQuery(forms.ModelForm):
	class Meta:
		model = ChuckFact
		fields = '__all__'
		widgets = {
			'searchString' : forms.TextInput(attrs={'class':'form-control', 'type':'text',
	 						 'placeholder':'Keyword'})
		}