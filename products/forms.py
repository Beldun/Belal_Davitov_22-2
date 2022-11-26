from django import forms


class ProductCreateForm(forms.Form):
    categories = forms.ChoiceField(choices=(
        (1, 'iPhone'),
        (2, 'AirPods'),
        (3, 'Mac'),
        (4, 'MacBook'),
        (5, 'Watch'),
    ))
    title = forms.CharField(max_length=150)
    price = forms.IntegerField()
    description = forms.CharField(widget=forms.Textarea)
    characteristics = forms.CharField(widget=forms.Textarea)


class ReviewCreateForm(forms.Form):
    text = forms.CharField(min_length=5)
    rate = forms.ChoiceField(choices=(
        ('1/5', '1/5'),
        ('2/5', '2/5'),
        ('3/5', '3/5'),
        ('4/5', '4/5'),
        ('5/5', '5/5')
    ))
