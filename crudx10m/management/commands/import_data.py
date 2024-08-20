from django.core.management.base import BaseCommand
from django.db import transaction
from django.core.paginator import Paginator
import csv
from crudx10m.const import DATASET_PATH
from crudx10m.models import (
    DemographicData,
    DemographicDataTest,
    Education,
    MaritalStatus,
    NativeCountry,
    Occupation,
    Race,
    Relationship,
    Sex,
    WorkClass,
)

# class Command(BaseCommand):
#     help = 'Import data into DemographicDataTest model'Language

#     def handle(self, *args, **kwargs):
#         file_path = DATASET_PATH
#         batch_size = 10000

#         with open(file_path, 'r') as file:
#             reader = csv.reader(file)
#             batch = []

#             for row in reader:
#                 batch.append(DemographicDataTest(
#                     age=int(row[0]),
#                     workclass=row[1] if row[1] != '?' else None,
#                     fnlwgt=int(row[2]),
#                     education=row[3],
#                     education_num=int(row[4]),
#                     marital_status=row[5],
#                     occupation=row[6] if row[6] != '?' else None,
#                     relationship=row[7],
#                     race=row[8],
#                     sex=row[9],
#                     capital_gain=int(row[10]),
#                     capital_loss=int(row[11]),
#                     hours_per_week=int(row[12]),
#                     native_country=row[13] if row[13] != '?' else None,
#                     income=row[14],
#                 ))

#                 if len(batch) == 5000:
#                     try:
#                         with transaction.atomic():
#                             DemographicDataTest.objects.bulk_create(batch, batch_size=1000)
#                             print(f"{len(batch)} created successfully")
#                         batch = []
#                     except Exception as e:
#                         print(f"Error creating batch: {e}")

#             if batch:
#                 with transaction.atomic():
#                     DemographicDataTest.objects.bulk_create(batch)

#         self.stdout.write(self.style.SUCCESS('Data successfully loaded into the database!'))


def copy_data_to_multiple_models():
    work_class = DemographicDataTest.objects.values_list(
        "workclass", flat=True
    ).distinct()
    education = DemographicDataTest.objects.values_list(
        "education", flat=True
    ).distinct()
    marital_status = DemographicDataTest.objects.values_list(
        "marital_status", flat=True
    ).distinct()
    occupation = DemographicDataTest.objects.values_list(
        "occupation", flat=True
    ).distinct()
    relationship = DemographicDataTest.objects.values_list(
        "relationship", flat=True
    ).distinct()
    race = DemographicDataTest.objects.values_list("race", flat=True).distinct()
    sex = DemographicDataTest.objects.values_list("sex", flat=True).distinct()
    native_country = DemographicDataTest.objects.values_list(
        "native_country", flat=True
    ).distinct()

    print("0")

    work_classes = []
    for i in work_class:
        if i == None:
            continue
        work_classes.append(WorkClass(label=i.strip().lower()))
    WorkClass.objects.bulk_create(work_classes)

    print("1")

    education_list = []
    for i in education:
        if i == None:
            continue
        education_list.append(Education(label=i.strip().lower()))
    Education.objects.bulk_create(education_list)

    print("2")

    occupation_list = []
    for i in occupation:
        if i == None:
            continue
        occupation_list.append(Occupation(label=i.strip().lower()))
    Occupation.objects.bulk_create(occupation_list)

    print("3")

    relationship_list = []
    for i in relationship:
        if i == None:
            continue
        relationship_list.append(Relationship(label=i.strip().lower()))
    Relationship.objects.bulk_create(relationship_list)

    print("4")

    race_list = []
    for i in race:
        if i == None:
            continue
        race_list.append(Race(label=i.strip().lower()))
    Race.objects.bulk_create(race_list)

    print("5")

    native_country_list = []
    for i in native_country:
        if i == None:
            continue
        native_country_list.append(NativeCountry(label=i.strip().lower()))
    NativeCountry.objects.bulk_create(native_country_list)

    print("6")

    sex_list = []
    for i in sex:
        if i == None:
            continue
        sex_list.append(Sex(label=i.strip().lower()))
    Sex.objects.bulk_create(sex_list)

    print("7")

    marital_status_list = []
    for i in marital_status:
        if i == None:
            continue
        marital_status_list.append(MaritalStatus(label=i.strip().lower()))
    MaritalStatus.objects.bulk_create(marital_status_list)

    print("7")


def copy_data_to_demographic_model():
    print("1")
    work_class_list = list(WorkClass.objects.all())
    work_class_dict = {
        work_class.label: work_class.id for work_class in work_class_list
    }
    print("2")

    education_list = list(Education.objects.all())
    education_dict = {education.label: education.id for education in education_list}

    print("3")
    occupation_list = list(Occupation.objects.all())
    occupation_dict = {
        occupation.label: occupation.id for occupation in occupation_list
    }

    print("4")
    relationship_list = list(Relationship.objects.all())
    relationship_dict = {
        relationship.label: relationship.id for relationship in relationship_list
    }

    print("5")
    race_list = list(Race.objects.all())
    race_dict = {race.label: race.id for race in race_list}

    print("6")
    native_country_list = list(NativeCountry.objects.all())
    native_country_dict = {
        native_country.label: native_country.id
        for native_country in native_country_list
    }

    print("7")
    sex_list = list(Sex.objects.all())
    sex_dict = {sex.label: sex.id for sex in sex_list}

    print("8")
    marital_status_list = list(MaritalStatus.objects.all())
    marital_status_dict = {
        MaritalStatus.label: marital_status.id for marital_status in marital_status_list
    }

    print("9")
    count = 0
    demographics_data_list = list()
    paginator = Paginator(
        DemographicDataTest.objects.all(), 2000
    )

    print("10")
    # for page_number in range(1, paginator.num_pages + 1):
    for page_number in range(4000, paginator.num_pages + 1):
        demographics_data = paginator.page(page_number).object_list
        for demographic_data in demographics_data:
            try:
                workclass_id = (
                    work_class_dict.get(
                        demographic_data.workclass.strip().lower(), None
                    )
                    if demographic_data.workclass
                    else None
                )

                education_id = (
                    education_dict.get(demographic_data.education.strip().lower(), None)
                    if demographic_data.education is not None
                    else None
                )

                marital_status_id = (
                    marital_status_dict.get(
                        demographic_data.marital_status.strip().lower(), None
                    )
                    if demographic_data.marital_status
                    else None
                )

                occupation_id = (
                    occupation_dict.get(
                        demographic_data.occupation.strip().lower(), None
                    )
                    if demographic_data.occupation
                    else None
                )

                relationship_id = (
                    relationship_dict.get(
                        demographic_data.relationship.strip().lower(), None
                    )
                    if demographic_data.relationship
                    else None
                )

                race_id = (
                    race_dict.get(demographic_data.race.strip().lower(), None)
                    if demographic_data.race
                    else None
                )

                sex_id = (
                    sex_dict.get(demographic_data.sex.strip().lower(), None)
                    if demographic_data.sex
                    else None
                )

                native_country_id = (
                    native_country_dict.get(
                        demographic_data.native_country.strip().lower(), None
                    )
                    if demographic_data.native_country
                    else None
                )

                demographic_data_dict = dict(
                    age=demographic_data.age,
                    fnlwgt=demographic_data.fnlwgt,
                    education_num=demographic_data.education_num,
                    capital_loss=demographic_data.capital_loss,
                    capital_gain=demographic_data.capital_gain,
                    hours_per_week=demographic_data.hours_per_week,
                    education_id=education_id,
                    marital_status=marital_status_id,
                    native_country_id=native_country_id,
                    occupation_id=occupation_id,
                    race_id=race_id,
                    relationship_id=relationship_id,
                    sex_id=sex_id,
                    workclass_id=workclass_id,
                )
                demographics_data_list.append(DemographicData(**demographic_data_dict))
                count += 1
                if count % 20000 == 0:
                    try:
                        with transaction.atomic():
                            DemographicData.objects.bulk_create(
                                demographics_data_list, batch_size=1000
                            )
                            demographics_data_list = list()
                            print(f"{count} records created successfully")
                    except Exception as e:
                        print(f"Error creating demographic data batch: {e}")
            except Exception as e:
                print(e)
                with transaction.atomic():
                    DemographicData.objects.bulk_create(
                        demographics_data_list, batch_size=400
                    )
    print("11")

class Command(BaseCommand):
    help = "Import data into DemographicDataTest model"

    def handle(self, *args, **kwargs):
        # copy_data_to_multiple_models()
        copy_data_to_demographic_model()
