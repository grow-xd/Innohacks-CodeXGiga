from transformers import MBartForConditionalGeneration, MBart50TokenizerFast
import requests
from transformers import pipeline
from datetime import datetime




language_codes = {
    'ar': 'ar_AR',
    'cs': 'cs_CZ',
    'de': 'de_DE',
    'en': 'en_XX',
    'es': 'es_XX',
    'et': 'et_EE',
    'fi': 'fi_FI',
    'fr': 'fr_XX',
    'gu': 'gu_IN',
    'hi': 'hi_IN',
    'it': 'it_IT',
    'ja': 'ja_XX',
    'kk': 'kk_KZ',
    'ko': 'ko_KR',
    'lt': 'lt_LT',
    'lv': 'lv_LV',
    'my': 'my_MM',
    'ne': 'ne_NP',
    'nl': 'nl_XX',
    'ro': 'ro_RO',
    'ru': 'ru_RU',
    'si': 'si_LK',
    'tr': 'tr_TR',
    'vi': 'vi_VN',
    'zh': 'zh_CN',
    'af': 'af_ZA',
    'az': 'az_AZ',
    'bn': 'bn_IN',
    'fa': 'fa_IR',
    'he': 'he_IL',
    'hr': 'hr_HR',
    'id': 'id_ID',
    'ka': 'ka_GE',
    'km': 'km_KH',
    'mk': 'mk_MK',
    'ml': 'ml_IN',
    'mn': 'mn_MN',
    'mr': 'mr_IN',
    'pl': 'pl_PL',
    'ps': 'ps_AF',
    'pt': 'pt_XX',
    'sv': 'sv_SE',
    'sw': 'sw_KE',
    'ta': 'ta_IN',
    'te': 'te_IN',
    'th': 'th_TH',
    'tl': 'tl_XX',
    'uk': 'uk_UA',
    'ur': 'ur_PK',
    'xh': 'xh_ZA',
    'gl': 'gl_ES',
    'sl': 'sl_SI'
}

def txt_translate(text,lang):
    print("(*************************)")
    article_en = text;
    model = MBartForConditionalGeneration.from_pretrained("SnypzZz/Llama2-13b-Language-translate")
    tokenizer = MBart50TokenizerFast.from_pretrained("SnypzZz/Llama2-13b-Language-translate", src_lang="en_XX")

    model_inputs = tokenizer(article_en, return_tensors="pt")
    generated_tokens = model.generate(
        **model_inputs,
        forced_bos_token_id=tokenizer.lang_code_to_id[language_codes[lang]]
    )
    return tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)
    
def gtxt_translate(text,lang):
    translator = Translator()

    translated_text = translator.translate(text, dest='hi').text
    print(translated_text)
    return translated_text

def new_translator(text):
    print(text)
    url = 'http://127.0.0.1:5000/translate'
    data = {
        'q': text,
		'source': "en",
		'target': "hi",
		'format': "text",
        'api_key': ""
    }

    # Make the API request
    response = requests.post(url, data=data)

    # Check the response
    if response.status_code == 200:
        print("^^^^^^^^^^^^^^^^^^^^^",response.json())
        res= response.json()
        return res.get('translatedText')
    else:
        print(f'Request failed with status code {response.status_code}')
        print(response.text)

def summarize_text(article, max_length=1000, min_length=30, do_sample=False):
        summarizer = pipeline("summarization", model="Falconsai/text_summarization")
        # Generate the summarized text
        summerized_text = summarizer(article, max_length=100, min_length=30, do_sample=False)
        summerized_text=summerized_text[0]['summary_text']
        return summerized_text

def ppttransform(url):
    
    current_datetime = datetime.now()
    formatted_datetime = current_datetime.strftime("%Y-%m-%d_%H-%M-%S")

    file_name = f"output_{formatted_datetime}.ppt"
    response = requests.get(url)
    if response.status_code == 200:
        with open(file_name, 'wb') as file:
            file.write(response.content)
        print(f"Download successful. Saved to {file_name}")
    else:
        print(f"Failed to download. Status code: {response.status_code}")


    files = {'file': open(file_name, 'rb')}
    url = 'http://127.0.0.1:5000/translate_file'
    data = {
        'api_key': "",
        'source': "en",
        'target': "hi",
    }

    # Make the API request
    response = requests.post(url,files=files, data=data)
    # Check the response
    if response.status_code == 200:
        print("^^^^^^^^^^^^^^^^^^^^^",response.json())
        res= response.json()

        return res.get('translatedFileUrl')
    else:
        print(f'Request failed with status code {response.status_code}')
        print(response.text)