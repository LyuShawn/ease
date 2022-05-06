import argparse
import re
from tqdm import tqdm


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input_path",
        type=str,
        default="/home/nchaso/EASE/downstreams/text-clustering/data/mewsc16/ja_sentences.txt",
    )
    parser.add_argument(
        "--output_path",
        type=str,
        default="/home/nchaso/EASE/downstreams/text-clustering/data/mewsc16/cleaned_ja_sentences.txt",
    )
    args = parser.parse_args()

    regex = re.compile(
        r"thumb\||right\||left\||upright=1\||náhled\||eta\||frame\||\d\d\dpx\||upright\||слева\||\d\d\dпкс\||"
    )

    # test codes
    """
    targets = [
        "thumb|200px|right|Orhan PamukL'escriptor turc és el guanyador del del , fet públic avui, a la una del migdia.",
        "náhled|Španělský král Juan CarlosKrál jim popřál šťastný nový rok 2008 a poobědval s nimi.",
        "eta|250px|Bakterioj de plej ofta kaŭzo de tuberkulozo, 'Mycobacterium tuberculosis'.",
        "thumb|left|250px|نقشهٔ محل زمین‌لرزهدر پی زمین‌لرزهٔ شدید و سونامی در سواحل غربی اندونزی، حداقل ۱۰۸ نفر کشته شده و صدها تن ناپدید گشتند.",
        "thumb|240px|1967年以来イスラエルが占領していたガザ地区NHKによると、イスラエルは、日本時間12日午後1時（現地時間、UTC+3、午前7時）、ガザ地区からの撤退を完了した。",
        "frame|rightGdyby wybory do Sejmu odbyły się pod koniec stycznia, wygrałaby je Platforma Obywatelska, uzyskując 27% głosów.",
        "thumb|left|upright|Andrzej Lepper'Niech CBA poda, od kogo się dowiedziało, że R. i K. chodzą po Warmii i Mazurach i oferują załatwianie jakichś spraw.",
        "слева|thumb|147пкс|Старт ракеты Atlas, фотоВ 19:00 ракета Atlas V с космическим аппаратом («Новые горизонты») на борту стартовала с мыса Канаверал.",
    ]

    expected_list = [
        "Orhan PamukL'escriptor turc és el guanyador del del , fet públic avui, a la una del migdia.",
        "Španělský král Juan CarlosKrál jim popřál šťastný nový rok 2008 a poobědval s nimi.",
        "Bakterioj de plej ofta kaŭzo de tuberkulozo, 'Mycobacterium tuberculosis'.",
        "نقشهٔ محل زمین‌لرزهدر پی زمین‌لرزهٔ شدید و سونامی در سواحل غربی اندونزی، حداقل ۱۰۸ نفر کشته شده و صدها تن ناپدید گشتند.",
        "1967年以来イスラエルが占領していたガザ地区NHKによると、イスラエルは、日本時間12日午後1時（現地時間、UTC+3、午前7時）、ガザ地区からの撤退を完了した。",
        "rightGdyby wybory do Sejmu odbyły się pod koniec stycznia, wygrałaby je Platforma Obywatelska, uzyskując 27% głosów.",
        "Andrzej Lepper'Niech CBA poda, od kogo się dowiedziało, że R. i K. chodzą po Warmii i Mazurach i oferują załatwianie jakichś spraw.",
        "Старт ракеты Atlas, фотоВ 19:00 ракета Atlas V с космическим аппаратом («Новые горизонты») на борту стартовала с мыса Канаверал.",
    ]
    for target, expected in zip(targets, expected_list):
        target = regex.sub("", target)
        assert expected == target, "expected[{0}], input[{1}]".format(expected, target)    
    """

    with open(args.input_path) as f:
        texts = [regex.sub("", s.strip()) for s in tqdm(f.readlines())]

    with open(args.output_path, mode="w") as f:
        f.write("\n".join(texts))


if __name__ == "__main__":
    main()
