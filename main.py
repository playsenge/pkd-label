def main():
    import requests

    kody = """
    PKD 49.10 Z
    PKD 49.31 Z
    PKD 49.32 Z
    PKD 49.39 Z
    PKD 49.42 Z
    PKD 50.10 Z
    PKD 50.30 Z
    PKD 51.10 Z
    PKD 52.21 Z
    PKD 52.22 A
    PKD 52.22 B
    PKD 52.23 Z
    PKD 53.10 Z
    PKD 53.20 Z
    PKD 55.10 Z
    PKD 55.20 Z
    PKD 55.30 Z
    PKD 55.90 Z
    PKD 56.10 A
    PKD 56.10 B
    PKD 56.21 Z
    PKD 56.29 Z
    PKD 56.30 Z
    """

    kody = kody.strip().split('\n')

    kody = [kod.lstrip('PKD ') for kod in kody]

    for kod in kody:
        url = f'https://www.pkd.com.pl/wyszukiwarka/pkd/{kod.replace(' ', '.')}.html'
        dane = requests.get(url).text.split('\n')
        linijka = [x for x in dane if x.startswith('<meta content="')][0].split('Prosta i szybka')[0][len('<meta content="'):]

        print('PKD', kod, '-', linijka)

if __name__ == '__main__':
    main()
