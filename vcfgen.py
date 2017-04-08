import csv
import vobject

with open('contacts.csv') as f:
    data = [tuple(line) for line in csv.reader(f)]

for name, number in data:
#    print(name)
#    print(number)
    j = vobject.vCard()
    o = j.add('fn')
    o.value = "{}" .format(name)
    o = j.add('n')
    o.value = vobject.vcard.Name( given = "{}" .format(name))
    o = j.add('tel')
    o.type_param = "cell"
    o.value = "{}" .format(number)
    print(j.serialize())
    out_file = name + ".vcf"
    fout = open(out_file, 'w')
    fout.write(j.serialize())
    fout.close()
