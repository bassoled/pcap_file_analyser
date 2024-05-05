import re
import zlib

def process_pcap_file(payload_information):
    try:
        # isolate file_info
        matches = re.finditer(r'\r\n\r\n', payload_information)

        for payload_information_match, match in enumerate(matches):
            payload_information_match = payload_information_match + 1
            file_info_raw = payload_information[:match.end()]
            print (file_info_raw)
        regex = "/?P&lt;'name&gt;.*?/: /?P&lt;value&gt;.*?/\n"
        file_info = dict(re.findall(regex, file_info_raw, re.UNICODE))
        return file_info
    except:
        return None
    if 'Content-Type' not in file_info:
        return None
    return file_info

def extracting_text_information(file_info, payload_information):
        text = None
        try:
            if 'text/html' in file_info['Content-Type']:
                text = payload_information[payload_information.index("\n\n")+4:]
                try:
                    if "Content-Encoding" in file_info.keys():
                        if file_info['Content-Encoding'] == "gzip":
                            text = zlib.decompress(text)
                    elif file_info['Content-Encoding'] == "deflate":
                        text = zlib.decompress(text)
                except: pass
        except:
            return None
        return text
