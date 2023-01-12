from datetime import datetime

from parcel.parcel import Parcel
from parcel.tracking import Tracking, Step
from parcel.info import Info


class Parser:
    def __init__(self, browser) -> None:
        self.browser = browser

    def find_raw_info(self):
        def find_fieldsets():
            return self.browser.browser.soup.find_all(['fieldset'])

        def find_tds(fieldsets):
            for item in fieldsets:
                try:
                    legend = item.find('legend')
                    if 'Detalle guía' in legend.text:
                        return item.find('table').find_all('td')
                except AttributeError:
                    continue
            else:
                raise ValueError("Could not find defined HTML structure")
        return find_tds(find_fieldsets())

    @property
    def info(self) -> Info:
        result = {}
        for element in self.find_raw_info():
            item = self.parse_info_field(element)
            result[item['field']] = item['value']
        return Info(
            result['Números principales'],
            result['Destinatario'],
            result['Dirección'],
            result['Teléfono'],
            result['Ciudad origen'],
            result['Ciudad destino'],
        )

    def parse_info_field(self, string) -> tuple:
        field = string.text.replace('\n', '').replace('                                ', ' ').split(':')[0].strip()
        value = string.text.replace('\n', '').replace('                                ', ' ').split(':')[1].strip()
        return {'field': field, 'value': value}

    def find_raw_tracking(self):
        def find_fieldsets():
            return self.browser.browser.soup.find_all(['fieldset'])
        def find_trs(fieldsets):
            for item in fieldsets:
                try:
                    h3 = item.find('h3')
                    if 'Seguimiento de la entrega' in h3.text:
                        return item.find('table').find('tbody').find_all('tr')
                except AttributeError:
                    continue
            else:
                raise ValueError("Could not find defined HTML structure")
        return find_trs(find_fieldsets())

    @property
    def tracking(self) -> Info:
        result = []
        for index, element in enumerate(self.find_raw_tracking()):
            tds = element.find_all('td')
            text_date = tds[0].text.replace('.', '').upper()
            date = datetime.strptime(text_date, '%d/%m/%Y %I:%M:%S %p')
            status = tds[1].text
            message = tds[2].text
            result.append([date, status, message])
        return Tracking(result)
