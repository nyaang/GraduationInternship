from fontTools.ttLib import TTFont
import base64
import io
import re,html

def multReplace(text, rpdict):
    rx = re.compile('|'.join(map(re.escape, rpdict)))
    return rx.sub(lambda match:rpdict[match.group(0)], text)
def decode58Fangchan(html,key):
    glyphdict = {
        'glyph00001': '0',
        'glyph00002': '1',
        'glyph00003': '2',
        'glyph00004': '3',
        'glyph00005': '4',
        'glyph00006': '5',
        'glyph00007': '6',
        'glyph00008': '7',
        'glyph00009': '8',
        'glyph00010': '9'
    }
    data = base64.b64decode(key)  #base64解码
    fonts = TTFont(io.BytesIO(data))  #生成二进制字节
    cmap = fonts.getBestCmap()  #十进制ascii码到字形名的对应{38006:'glyph00002',...}
    chrMapNum = {}  #将变为{‘龥’:'1',...}
    for asc in cmap:
        chrMapNum[chr(asc)] = glyphdict[cmap[asc]]

    return multReplace(html,chrMapNum)
def decode58main(f):
    text = html.unescape(f.decode())  #将&#x958f;室变为閏室
    key = re.findall(r"base64,(.*)'\).format", text)[0]  #用正则表达式提取AAE..AAA
    dehtml = decode58Fangchan(text, key)
    return dehtml