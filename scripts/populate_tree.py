# familytree/scripts/populate_tree.py
from django.core.management.base import BaseCommand
from familytree.models import FamilyMember, Relationship


class Command(BaseCommand):
    help = 'Populate family tree from familyData.txt'

    def handle(self, *args, **kwargs):
        family = []
        with open('familyData.txt') as file:
            lines = file.readlines()
            for line in lines:
                parts = line.strip().split(" - ")
                id = parts[0]
                name = parts[1].split(",")[0].strip()
                partner_name = parts[1].split(",")[1].strip() if len(parts[1].split(",")) > 1 else None

                member = FamilyMember.objects.create(id=id, name=name, partner=partner_name)
                family.append(member)

        for i in range(len(family)):
            id = family[i].id
            children_count = 0
            for j in range(len(family)):
                id_format = f'{id}.{children_count + 1}'
                if family[j].id.startswith(id_format):
                    child = family[j]
                    Relationship.objects.create(parent=family[i], child=child)
                    children_count += 1

        self.stdout.write(self.style.SUCCESS('Successfully populated family tree'))
