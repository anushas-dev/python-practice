import featuretools as ft

es = ft.demo.load_mock_customer(return_entityset=True)
print(es)