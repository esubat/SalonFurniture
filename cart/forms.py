from django import forms

#here I restricted individual users from ordering more that 10 items per furniture
QUANTITY_CHOICE = [(i , str(i)) for i in range(1,11)] 

class CartAddForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=QUANTITY_CHOICE,
                                      coerce=int)
    override = forms.BooleanField(required=False,
                                  initial=False,
                                  widget=forms.HiddenInput)
    