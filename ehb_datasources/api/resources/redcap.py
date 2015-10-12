import json

from flask_restful import Resource, request
from ehb_datasources.drivers.redcap.driver import ehbDriver
from datetime import datetime
form_types = {
    'record_list_form': 'rlf',
    'sub_record_form': 'srf',
    'sub_record_selection_form': 'srsf'
}


class Redcap(Resource):
    def post(self, form_type=None):
        data = json.loads(request.data)
        # Get Driver required objects here:
        url = data['url']
        user = ''  # not needed for redcap
        password = data['password']
        secure = data['secure']
        # Get protocol configuration
        protocol_configuration = ''
        driver = ehbDriver(
            url=url,
            password=password,
            secure=secure)
        driver.configure(protocol_configuration)
        if form_type:
            if form_type == 'record_list_form':
                record_urls = data['record_urls']
                records = data['records']
                labels = data['labels']

                # required: record_urls, records, labels
                form = driver.recordListForm(record_urls, records, labels)
                return {"form": form}
            elif form_type == 'sub_record_form':
                # subRecordForm(self, external_record, form_spec='', *args, **kwargs):
                # required: external_record, form_spec
                form = driver.subRecordForm(er, '')
                return {"form": form}
            elif form_type == 'sub_record_selection_form':
                pass

            # try:
            #     form = form_types[form_type]
            # except KeyError:
            #     return {"error": "form type supplied not recognized"}
            return {"form": "form type supplied not recognized"}
        else:
            return {"hello": "from redcap"}
