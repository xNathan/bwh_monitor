import os

import requests


def kb_to(kbs, unit):
    kb = 1 * 1024
    mb = kb * 1024
    gb = mb * 1024
    unit_map = dict(kb=kb, mb=mb, gb=gb)
    return kbs / unit_map[unit]


class Monitor(object):
    def __init__(self, veid, api_key):
        self.identity = {
            "veid": veid,
            "api_key": api_key
        }
        self.host = "https://api.64clouds.com/v1/"

    def _request(self, endpoint, params=None):
        url = self._to_api_url(endpoint)

        return requests.get(url, params=self.identity)

    def _to_api_url(self, endpoint):
        return self.host + endpoint

    def get_service_info(self):
        endpoint = "getServiceInfo"
        res = self._request(endpoint)
        return res.json()

    def get_remain_data(self, service_info):
        data_next_reset = service_info["data_next_reset"]
        data_counter = service_info["data_counter"]
        plan_monthly_data = service_info["plan_monthly_data"]
        return {"total": plan_monthly_data, "used": data_counter, "reset": data_next_reset}


def main():
    bwh_id = os.environ.get("BWH_ID")
    bwh_api_key = os.environ.get("BWH_API_KEY")

    if bwh_id is None or bwh_api_key is None:
        print("ERROR: Pleases set BWH_ID and BWH_API_KEY")
        exit(1)

    monitor = Monitor(bwh_id, bwh_api_key)
    info = monitor.get_service_info()
    remain_data = monitor.get_remain_data(info)

    unit = "gb"
    print("total", kb_to(remain_data["total"], unit), unit)
    print("used", kb_to(remain_data["used"], unit), unit)


if __name__ == "__main__":
    main()
