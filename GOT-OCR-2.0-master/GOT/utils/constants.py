CONTROLLER_HEART_BEAT_EXPIRATION = 30
WORKER_HEART_BEAT_INTERVAL = 15

LOGDIR = "log"

IGNORE_INDEX = -100
# DEFAULT_PAD_TOKEN = "[PAD]"

DEFAULT_PAD_TOKEN = "<|endoftext|>"
DEFAULT_EOS_TOKEN = "</s>"
DEFAULT_BOS_TOKEN = "</s>"
DEFAULT_UNK_TOKEN = "<unk>"
DEFAULT_IMAGE_TOKEN = "<image>"
DEFAULT_BOX_TOKEN = "<box>"

DEFAULT_IMAGE_PATCH_TOKEN = '<imgpad>'

DEFAULT_IM_START_TOKEN = '<img>'
DEFAULT_IM_END_TOKEN = '</img>'



data_array = ["BL","BY","DX","DZ","FG","FZ","GL","HF","HN","HX","JX","KB","LC","LG","LK","LZ","MK","PH","PL","PN","PQ","QL","QS","RB","RY","SK","SR","SX","SZ","WJ","WX","WY","WZ","XZ","YB","YG","YN","ZC","ZH","ZJ","ZX","ZY"]

CONVERSATION_DATA = {
    'data_BL': {
        'images': '/home/cncs-ai/work/deep_learning/GOT-OCR2.0/dataset/pattern_random/',
        'annotations': '/home/cncs-ai/work/deep_learning/GOT-OCR2.0/dataset/pattern_random/bl.json',
    },
    'data_BY': {
        'images': '/home/cncs-ai/work/deep_learning/GOT-OCR2.0/dataset/pattern_random/',
        'annotations': '/home/cncs-ai/work/deep_learning/GOT-OCR2.0/dataset/pattern_random/by.json',
    },
    'data_DX': {
        'images': '/home/cncs-ai/work/deep_learning/GOT-OCR2.0/dataset/pattern_random/',
        'annotations': '/home/cncs-ai/work/deep_learning/GOT-OCR2.0/dataset/pattern_random/dx.json',
    },
    'data_DZ': {
        'images': '/home/cncs-ai/work/deep_learning/GOT-OCR2.0/dataset/pattern_random/',
        'annotations': '/home/cncs-ai/work/deep_learning/GOT-OCR2.0/dataset/pattern_random/dz.json',
    },
    'data_FG': {
        'images': '/home/cncs-ai/work/deep_learning/GOT-OCR2.0/dataset/pattern_random/',
        'annotations': '/home/cncs-ai/work/deep_learning/GOT-OCR2.0/dataset/pattern_random/fg.json',
    },
    'data_FZ': {
        'images': '/home/cncs-ai/work/deep_learning/GOT-OCR2.0/dataset/pattern_random/',
        'annotations': '/home/cncs-ai/work/deep_learning/GOT-OCR2.0/dataset/pattern_random/fz.json',
    },
    'data_GL': {
        'images': '/home/cncs-ai/work/deep_learning/GOT-OCR2.0/dataset/pattern_random/',
        'annotations': '/home/cncs-ai/work/deep_learning/GOT-OCR2.0/dataset/pattern_random/gl.json',
    },
    'data_HF': {
        'images': '/home/cncs-ai/work/deep_learning/GOT-OCR2.0/dataset/pattern_random/',
        'annotations': '/home/cncs-ai/work/deep_learning/GOT-OCR2.0/dataset/pattern_random/hf.json',
    },
    'data_HN': {
        'images': '/home/cncs-ai/work/deep_learning/GOT-OCR2.0/dataset/pattern_random/',
        'annotations': '/home/cncs-ai/work/deep_learning/GOT-OCR2.0/dataset/pattern_random/hn.json',
    },
    'data_HX': {
        'images': '/home/cncs-ai/work/deep_learning/GOT-OCR2.0/dataset/pattern_random/',
        'annotations': '/home/cncs-ai/work/deep_learning/GOT-OCR2.0/dataset/pattern_random/hx.json',
    },
    'data_JX': {
        'images': '/home/cncs-ai/work/deep_learning/GOT-OCR2.0/dataset/pattern_random/',
        'annotations': '/home/cncs-ai/work/deep_learning/GOT-OCR2.0/dataset/pattern_random/jx.json',
    },
    'data_KB': {
        'images': '/home/cncs-ai/work/deep_learning/GOT-OCR2.0/dataset/pattern_random/',
        'annotations': '/home/cncs-ai/work/deep_learning/GOT-OCR2.0/dataset/pattern_random/kb.json',
    },
    'data_LC': {
        'images': '/home/cncs-ai/work/deep_learning/GOT-OCR2.0/dataset/pattern_random/',
        'annotations': '/home/cncs-ai/work/deep_learning/GOT-OCR2.0/dataset/pattern_random/lc.json',
    },
    'data_LG': {
        'images': '/home/cncs-ai/work/deep_learning/GOT-OCR2.0/dataset/pattern_random/',
        'annotations': '/home/cncs-ai/work/deep_learning/GOT-OCR2.0/dataset/pattern_random/lg.json',
    },
    'data_LK': {
        'images': '/home/cncs-ai/work/deep_learning/GOT-OCR2.0/dataset/pattern_random/',
        'annotations': '/home/cncs-ai/work/deep_learning/GOT-OCR2.0/dataset/pattern_random/lk.json',
    },
    'data_LZ': {
        'images': '/home/cncs-ai/work/deep_learning/GOT-OCR2.0/dataset/pattern_random/',
        'annotations': '/home/cncs-ai/work/deep_learning/GOT-OCR2.0/dataset/pattern_random/lz.json',
    },
    'data_MK': {
        'images': '/home/cncs-ai/work/deep_learning/GOT-OCR2.0/dataset/pattern_random/',
        'annotations': '/home/cncs-ai/work/deep_learning/GOT-OCR2.0/dataset/pattern_random/mk.json',
    },
    'data_PH': {
        'images': '/home/cncs-ai/work/deep_learning/GOT-OCR2.0/dataset/pattern_random/',
        'annotations': '/home/cncs-ai/work/deep_learning/GOT-OCR2.0/dataset/pattern_random/ph.json',
    },
    'data_PL': {
        'images': '/home/cncs-ai/work/deep_learning/GOT-OCR2.0/dataset/pattern_random/',
        'annotations': '/home/cncs-ai/work/deep_learning/GOT-OCR2.0/dataset/pattern_random/pl.json',
    },
    'data_PN': {
        'images': '/home/cncs-ai/work/deep_learning/GOT-OCR2.0/dataset/pattern_random/',
        'annotations': '/home/cncs-ai/work/deep_learning/GOT-OCR2.0/dataset/pattern_random/pn.json',
    },
    'data_PQ': {
        'images': '/home/cncs-ai/work/deep_learning/GOT-OCR2.0/dataset/pattern_random/',
        'annotations': '/home/cncs-ai/work/deep_learning/GOT-OCR2.0/dataset/pattern_random/pq.json',
    },
    'data_QL': {
        'images': '/home/cncs-ai/work/deep_learning/GOT-OCR2.0/dataset/pattern_random/',
        'annotations': '/home/cncs-ai/work/deep_learning/GOT-OCR2.0/dataset/pattern_random/ql.json',
    },
    'data_QS': {
        'images': '/home/cncs-ai/work/deep_learning/GOT-OCR2.0/dataset/pattern_random/',
        'annotations': '/home/cncs-ai/work/deep_learning/GOT-OCR2.0/dataset/pattern_random/qs.json',
    },
    'data_RB': {
        'images': '/home/cncs-ai/work/deep_learning/GOT-OCR2.0/dataset/pattern_random/',
        'annotations': '/home/cncs-ai/work/deep_learning/GOT-OCR2.0/dataset/pattern_random/rb.json',
    },
    'data_RY': {
        'images': '/home/cncs-ai/work/deep_learning/GOT-OCR2.0/dataset/pattern_random/',
        'annotations': '/home/cncs-ai/work/deep_learning/GOT-OCR2.0/dataset/pattern_random/ry.json',
    },
    'data_SK': {
        'images': '/home/cncs-ai/work/deep_learning/GOT-OCR2.0/dataset/pattern_random/',
        'annotations': '/home/cncs-ai/work/deep_learning/GOT-OCR2.0/dataset/pattern_random/sk.json',
    },
    'data_SR': {
        'images': '/home/cncs-ai/work/deep_learning/GOT-OCR2.0/dataset/pattern_random/',
        'annotations': '/home/cncs-ai/work/deep_learning/GOT-OCR2.0/dataset/pattern_random/sr.json',
    },
    'data_SX': {
        'images': '/home/cncs-ai/work/deep_learning/GOT-OCR2.0/dataset/pattern_random/',
        'annotations': '/home/cncs-ai/work/deep_learning/GOT-OCR2.0/dataset/pattern_random/sx.json',
    },
    'data_SZ': {
        'images': '/home/cncs-ai/work/deep_learning/GOT-OCR2.0/dataset/pattern_random/',
        'annotations': '/home/cncs-ai/work/deep_learning/GOT-OCR2.0/dataset/pattern_random/sz.json',
    },
    'data_WJ': {
        'images': '/home/cncs-ai/work/deep_learning/GOT-OCR2.0/dataset/pattern_random/',
        'annotations': '/home/cncs-ai/work/deep_learning/GOT-OCR2.0/dataset/pattern_random/wj.json',
    },
    'data_WX': {
        'images': '/home/cncs-ai/work/deep_learning/GOT-OCR2.0/dataset/pattern_random/',
        'annotations': '/home/cncs-ai/work/deep_learning/GOT-OCR2.0/dataset/pattern_random/wx.json',
    },
    'data_WY': {
        'images': '/home/cncs-ai/work/deep_learning/GOT-OCR2.0/dataset/pattern_random/',
        'annotations': '/home/cncs-ai/work/deep_learning/GOT-OCR2.0/dataset/pattern_random/wy.json',
    },
    'data_WZ': {
        'images': '/home/cncs-ai/work/deep_learning/GOT-OCR2.0/dataset/pattern_random/',
        'annotations': '/home/cncs-ai/work/deep_learning/GOT-OCR2.0/dataset/pattern_random/wz.json',
    },
    'data_XZ': {
        'images': '/home/cncs-ai/work/deep_learning/GOT-OCR2.0/dataset/pattern_random/',
        'annotations': '/home/cncs-ai/work/deep_learning/GOT-OCR2.0/dataset/pattern_random/xz.json',
    },
    'data_YB': {
        'images': '/home/cncs-ai/work/deep_learning/GOT-OCR2.0/dataset/pattern_random/',
        'annotations': '/home/cncs-ai/work/deep_learning/GOT-OCR2.0/dataset/pattern_random/yb.json',
    },
    'data_YG': {
        'images': '/home/cncs-ai/work/deep_learning/GOT-OCR2.0/dataset/pattern_random/',
        'annotations': '/home/cncs-ai/work/deep_learning/GOT-OCR2.0/dataset/pattern_random/yg.json',
    },
    'data_YN': {
        'images': '/home/cncs-ai/work/deep_learning/GOT-OCR2.0/dataset/pattern_random/',
        'annotations': '/home/cncs-ai/work/deep_learning/GOT-OCR2.0/dataset/pattern_random/yn.json',
    },
    'data_ZC': {
        'images': '/home/cncs-ai/work/deep_learning/GOT-OCR2.0/dataset/pattern_random/',
        'annotations': '/home/cncs-ai/work/deep_learning/GOT-OCR2.0/dataset/pattern_random/zc.json',
    },
    'data_ZH': {
        'images': '/home/cncs-ai/work/deep_learning/GOT-OCR2.0/dataset/pattern_random/',
        'annotations': '/home/cncs-ai/work/deep_learning/GOT-OCR2.0/dataset/pattern_random/zh.json',
    },
    'data_ZJ': {
        'images': '/home/cncs-ai/work/deep_learning/GOT-OCR2.0/dataset/pattern_random/',
        'annotations': '/home/cncs-ai/work/deep_learning/GOT-OCR2.0/dataset/pattern_random/zj.json',
    },
    'data_ZX': {
        'images': '/home/cncs-ai/work/deep_learning/GOT-OCR2.0/dataset/pattern_random/',
        'annotations': '/home/cncs-ai/work/deep_learning/GOT-OCR2.0/dataset/pattern_random/zx.json',
    },
    'data_ZY': {
        'images': '/home/cncs-ai/work/deep_learning/GOT-OCR2.0/dataset/pattern_random/',
        'annotations': '/home/cncs-ai/work/deep_learning/GOT-OCR2.0/dataset/pattern_random/zy.json',
    }
}