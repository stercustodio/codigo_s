from pycep_correios import WebService, get_address_from_cep
import unicodedata


class AddressTools():
    @staticmethod
    def get_address(data):
        reference = get_address_from_cep(data, webservice=WebService.VIACEP)
        vectors = ['cep', 'logradouro', 'bairro', 'cidade', 'uf']
        aux = reference.copy()
        for key in aux:
            if key not in vectors:
                del reference[key]

        reference = AddressTools.addresstranslator(**reference)

        return reference

    @staticmethod
    def addresstranslator(cep, logradouro, bairro, cidade, uf):
        addr = dict()

        addr["zip_code"] = cep
        addr["place"] = logradouro
        addr["neighborhood"] = bairro
        addr["city"] = cidade
        addr["district"] = uf

        addr["zip_code"] = addr.get("zip_code").replace("-", "")

        return addr
        

    @staticmethod
    def normalizer(data, vector):
        value = data.get(vector)
        
        if value:
            data[vector] = unicodedata.normalize('NFD', value).encode('ascii', 'ignore')
            data[vector] = data.get(vector).decode().upper().strip()
            count = data.get(vector).count("  ")
            for _ in range(count-1):
                data[vector] = data.get(vector).replace("  ", " ")
        
        return data.get(vector)

    @staticmethod
    def normalized_match(data, reference):
        for key in data.keys():
            if AddressTools.normalizer(data, key) != AddressTools.normalizer(reference, key):
                return key, False
        
        return key, True
        