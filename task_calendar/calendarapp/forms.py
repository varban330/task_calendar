from django import forms

class DateForm(forms.Form):
    Options = (('1', 'January'),('2', 'February'),('3', 'March'),('4', 'April'),('5', 'May'),('6', 'June'),('7', 'July'),('8', 'August'),('9', 'September'),('10', 'October'),('11', 'November'),('12', 'December'))
    month = forms.ChoiceField(label='Month', widget=forms.Select, choices=Options)
    year = forms.IntegerField()

    class Meta:
        fields = ["month","year"]
