from django import forms

class ProductForm(forms.Form):

    BRAND_LIST = [('Dior', 'Dior'),
                  ('Yves Saint Laurent', 'Yves Saint Laurent'),
                  ('Lamer', 'Lamer'),
                  ('Estée Lauder', 'Estée Lauder'),
                  ('Chanel', 'Chanel'),
                  ]

    COLLECTION_LIST = [('spring', 'spring'),
                  ('summer', 'summer'),
                  ('winter', 'winter'),
                  ('music festival', 'music festival'),
                  ('Christmas', 'Christmas'),
                  ('Halloween', 'Halloween'),
                  ]

    TYPE_LIST = [('Base Makeup', 'Base Makeup'),
                 ('Foundation', 'Foundation'),
                 ('Powder', 'Powder'),
                 ('Highligh', 'Highligh'),
                 ('Bronzer', 'Bronzer'),
                 ('Eye Shadow', 'Eye Shadow'),
                 ('Blush on', 'Blush on'),
                 ]

    id = forms.CharField(max_length=13, label="รหัสสินค้า",
                         required=True, widget=forms.TextInput(attrs={'size': '15'}))

    brand = forms.CharField(max_length=30, label="ชื่อแบรนด์",  required=True, widget=forms.Select(choices=BRAND_LIST))

    model = forms.CharField(max_length=30, label="ชื่อรุ่น", required=True, widget=forms.TextInput(attrs={'size': '35'}))

    color = forms.CharField(max_length=30, label="คอเลคชั่น", required=True, widget=forms.RadioSelect(choices=COLLECTION_LIST))

    type = forms.CharField(max_length=30, label="ประเภท", required=True, widget=forms.Select(choices=TYPE_LIST))

    price = forms.IntegerField(label="ราคา", required=True, widget=forms.NumberInput(
        attrs={'size': '35', 'min': '2000', 'max': '1000000'}))