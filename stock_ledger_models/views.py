import json

from django.db import IntegrityError
from .models import Location, stg_trn_data, stg_trn_data_del_records
from django.http import JsonResponse

from django.views.decorators.csrf import csrf_exempt

def count(request):
    count1 = stg_trn_data.objects.filter(PROCESS_IND="N").count()
    count2 = stg_trn_data.objects.filter(PROCESS_IND="I").count()
    count3 = stg_trn_data.objects.filter(PROCESS_IND="E").count()
    count4 = stg_trn_data.objects.filter(PROCESS_IND="Y").count()
    count5 = stg_trn_data_del_records.objects.all().count()

    return JsonResponse(
        {
            "count1": f"count of indicator N at STG_TRN_DATA table: {count1}",
            "count2": f"count of indicator N at STG_TRN_DATA table: {count2}",
            "count3": f"count of indicator N at STG_TRN_DATA table: {count3}",
            "count4": f"count of indicator N at STG_TRN_DATA table: {count4}",
            "count5": f"count of indicator N at STG_TRN_DATA table: {count5}"
        }
    )



@csrf_exempt
def home(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        json_data = data.get("json_data")
        data_list = []

        for item in json_data:
            TRAN_SEQ_NO=item.get("TRAN_SEQ_NO", None)
            PROCESS_IND=item.get("PROCESS_IND", None)
            ITEM=item.get("ITEM", None)
            REF_ITEM=item.get("REF_ITEM", None)
            REF_ITEM_TYPE=item.get("REF_ITEM_TYPE", None)
            LOCATION_TYPE=item.get("LOCATION_TYPE", None)
            LOCATION=item.get("LOCATION", None)
            
            TRN_DATE=item.get("TRN_DATE", None)
            TRN_TYPE=item.get("TRN_TYPE", None)
            QTY=item.get("QTY", None)
            PACK_QTY=item.get("PACK_QTY", None)
            PACK_COST=item.get("PACK_COST", None)
            PACK_RETAIL=item.get("PACK_RETAIL", None)
            UNIT_COST=item.get("UNIT_COST", None)
            UNIT_RETAIL=item.get("UNIT_RETAIL", None)
            TOTAL_COST=item.get("TOTAL_COST", None)
            TOTAL_RETAIL=item.get("TOTAL_RETAIL", None)
            REF_NO1=item.get("REF_NO1", None)
            REF_NO2=item.get("REF_NO2", None)
            REF_NO3=item.get("REF_NO3", None)
            REF_NO4=item.get("REF_NO4", None)
            AREF=item.get("AREF", None)
            CURRENCY=item.get("CURRENCY", None)
            CREATE_DATETIME=item.get("CREATE_DATETIME", None)
            CREATE_ID=item.get("CREATE_ID", None)
            REV_NO=item.get("REV_NO", None)
            REV_TRN_NO=item.get("REV_TRN_NO", None)

            values = stg_trn_data(
                TRAN_SEQ_NO=TRAN_SEQ_NO,
                PROCESS_IND=PROCESS_IND,
                ITEM=ITEM,
                REF_ITEM=REF_ITEM,
                REF_ITEM_TYPE=REF_ITEM_TYPE,
                LOCATION_TYPE=LOCATION_TYPE,
                LOCATION=LOCATION,
                TRN_DATE=TRN_DATE,
                TRN_TYPE=TRN_TYPE,
                QTY=QTY if QTY !="NULL" else None,
                PACK_QTY=PACK_QTY if PACK_QTY !="NULL" else None,
                PACK_COST=PACK_COST if PACK_COST !="NULL" else None,
                PACK_RETAIL=PACK_RETAIL if PACK_RETAIL !="NULL" else None,
                UNIT_COST=UNIT_COST if UNIT_COST !="NULL" else None,
                UNIT_RETAIL=UNIT_RETAIL if UNIT_RETAIL !="NULL" else None ,
                TOTAL_COST=TOTAL_COST if TOTAL_COST !="NULL" else None   ,
                TOTAL_RETAIL=TOTAL_RETAIL if TOTAL_RETAIL !="NULL" else None,
                REF_NO1=REF_NO1,
                REF_NO2=REF_NO2,
                REF_NO3=REF_NO3,
                REF_NO4=REF_NO4,
                AREF=AREF,
                CURRENCY=CURRENCY,
                CREATE_DATETIME=CREATE_DATETIME,
                CREATE_ID=CREATE_ID,
                REV_NO=REV_NO if REV_NO !="NULL" else None,
                REV_TRN_NO=REV_TRN_NO if REV_TRN_NO !="NULL" else REV_TRN_NO
            )

            data_list.append(values)

        try:
            stg_trn_data.objects.bulk_create(data_list)
        except IntegrityError:
            return JsonResponse({"status": 500, "message": "TRAN_SEQ_NO must be unique"})
        except ValueError:
            return JsonResponse({"status": 500, "message": "error"})
        except Exception as error:
            return JsonResponse({"status": 500, "message": str(error)})
        return JsonResponse({"status": 201, "message": "Data Inserted"})
