from requests_html import HTMLSession
import json

GCP_URL = 'https://www.gstatic.com/ipranges/cloud.json'
AWS_URL = 'https://ip-ranges.amazonaws.com/ip-ranges.json'

japanIpRanges = []
koreaIpRanges = []
taiwanIpRanges = []
singaporeIpRanges = []
australiaIpRanges = []
useIpRanges = []
uswIpRanges = []
euIpRanges = []
meIpRanges = []

def main():
    session = HTMLSession()
    response = session.get(GCP_URL)

    content = json.loads(response.content)
    for data in content['prefixes']:
        if data['service'] != 'Google Cloud':
            continue
        if data.get('ipv4Prefix') is None:
            continue
        get_ip_range(data)

    print('JAPAN:')
    for ip in japanIpRanges:
        print(ip)

    print('\nKOREA:')
    for ip in koreaIpRanges:
        print(ip)
    
    print('\nSINGAPORE:')
    for ip in singaporeIpRanges:
        print(ip)
    
    print('\nAUSTRALIA:')
    for ip in australiaIpRanges:
        print(ip)
    
    print('\nUS-EAST:')
    for ip in useIpRanges:
        print(ip)
    
    print('\nUS-WEST:')
    for ip in uswIpRanges:
        print(ip)
    
    print('\nMIDDLE EAST:')
    for ip in meIpRanges:
        print(ip)

def get_ip_range(data):
    if data['scope'] == 'asia-northeast1':
        japanIpRanges.append(data['ipv4Prefix'])
    elif data['scope'] == 'asia-east1':
        koreaIpRanges.append(data['ipv4Prefix'])
    elif data['scope'] == 'asia-southeast1' or data['scope'] == 'asia-southeast2':
        singaporeIpRanges.append(data['ipv4Prefix'])
    elif data['scope'] == 'australia-southeast1':
        australiaIpRanges.append(data['ipv4Prefix'])
    elif data['scope'] == 'us-east1':
        useIpRanges.append(data['ipv4Prefix'])
    elif data['scope'] == 'us-west1' or data['scope'] == 'us-west2':
        uswIpRanges.append(data['ipv4Prefix'])
    elif data['scope'] == 'europe-west6':
        euIpRanges.append(data['ipv4Prefix'])
    elif data['scope'] == 'me-central1' or data['scope'] == 'me-central2' or data['scope'] == 'me-west1':
        meIpRanges.append(data['ipv4Prefix'])

if __name__ == "__main__":
    main()