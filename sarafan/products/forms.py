from django import forms

from products.models import Shopping


class ShoppingForm(forms.ModelForm):
    class Meta:
        model = Shopping
        fields = ['product', 'quantity']

    def __init__(self, *args, **kwargs):
        super(ShoppingForm, self).__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            self.fields['product'].widget = forms.HiddenInput()

    def clean_quantity(self):
        quantity = self.cleaned_data.get('quantity')
        if quantity <= 0:
            raise forms.ValidationError('Количество должно быть больше нуля.')
        return quantity
