cmUgis=[160,205,193,201,178,201,211,150,205,165]
colisUgis=[round(cm/2.54, 2) for cm in cmUgis]
print(colisUgis)
txtUgis=['Aukstas' if i>=180 else 'Vidutinis' if i>=160 else 'Zemas' for i in cmUgis]
print(txtUgis)