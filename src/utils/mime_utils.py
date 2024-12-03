import magic

MIME_MAPPING = {
    "image/jpeg": [".jpg", ".jpeg"],
    "image/png": [".png"],
    "image/gif": [".gif"],
    "image/bmp": [".bmp"],
    "image/webp": [".webp"],
    "image/svg+xml": [".svg"],
    "image/tiff": [".tif", ".tiff"],
    "image/heif": [".heif", ".heic"],
    "image/x-icon": [".ico"],
    "image/vnd.microsoft.icon": [".ico"],
    "application/pdf": [".pdf"],
    "text/plain": [".txt"],
    "text/html": [".html", ".htm"],
    "text/css": [".css"],
    "text/javascript": [".js"],
    "application/json": [".json"],
    "application/xml": [".xml"],
    "application/zip": [".zip"],
    "application/x-rar-compressed": [".rar"],
    "application/x-tar": [".tar"],
    "application/gzip": [".gz"],
    "application/x-7z-compressed": [".7z"],
    "audio/mpeg": [".mp3"],
    "audio/wav": [".wav"],
    "audio/ogg": [".ogg"],
    "audio/mp4": [".m4a"],
    "audio/x-aiff": [".aiff", ".aif"],
    "audio/x-flac": [".flac"],
    "audio/x-ms-wma": [".wma"],
    "video/mp4": [".mp4"],
    "video/x-msvideo": [".avi"],
    "video/x-matroska": [".mkv"],
    "video/ogg": [".ogv"],
    "video/webm": [".webm"],
    "application/vnd.ms-excel": [".xls", ".xlsx"],
    "application/vnd.openxmlformats-officedocument.wordprocessingml.document": [".docx"],
    "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet": [".xlsx"],
    "application/vnd.ms-powerpoint": [".ppt", ".pptx"],
    "application/vnd.oasis.opendocument.text": [".odt"],
    "application/vnd.oasis.opendocument.spreadsheet": [".ods"],
    "application/vnd.oasis.opendocument.presentation": [".odp"],
    "application/x-shockwave-flash": [".swf"],
    "application/octet-stream": [".bin", ".exe"],
    "application/x-www-form-urlencoded": [".url"],
    "application/x-font-ttf": [".ttf"],
    "application/x-font-woff": [".woff"],
    "application/x-font-woff2": [".woff2"],
    "application/vnd.ms-fontobject": [".eot"],
    "application/x-mobipocket-ebook": [".mobi"],
    "application/epub+zip": [".epub"],
    "application/x-iso9660-image": [".iso"],
    "application/x-apple-diskimage": [".dmg"],
    "application/x-bzip": [".bz"],
    "application/x-bzip2": [".bz2"],
    "application/x-cpio": [".cpio"],
    "application/x-lzma": [".lzma"],
    "application/x-lzop": [".lzo"],
    "application/x-zstd": [".zst"],
    "application/x-xz": [".xz"],
    "application/x-rar": [".rar"],
    "application/x-tar": [".tar"],
    "text/csv": [".csv"],
    "application/vnd.ms-publisher": [".pub"],
    "application/x-vnd.oasis.opendocument.text": [".odt"],
    "application/x-vnd.oasis.opendocument.presentation": [".odp"],
    "application/x-vnd.oasis.opendocument.spreadsheet": [".ods"],
    "application/x-7z-compressed": [".7z"],
    "text/markdown": [".md", ".markdown"],
    "application/vnd.apple.keynote": [".key"],
    "application/vnd.apple.pages": [".pages"],
    "application/vnd.apple.numbers": [".numbers"],
    "application/vnd.ms-officetheme": [".thmx"],
    "application/vnd.ms-excel.sheet.macroEnabled.12": [".xlsm"],
    "application/vnd.openxmlformats-officedocument.presentationml.presentation": [".pptx"],
    "application/vnd.openxmlformats-officedocument.presentationml.slideshow": [".ppsx"],
    "application/vnd.openxmlformats-officedocument.wordprocessingml.template": [".dotx"],
    "application/vnd.openxmlformats-officedocument.spreadsheetml.template": [".xltx"],
    "application/vnd.openxmlformats-officedocument.presentationml.template": [".potx"],
    "application/vnd.ms-excel.sheet.binary.macroEnabled.12": [".xlsb"],
    "application/vnd.ms-excel.addin.macroEnabled.12": [".xlam"],
    "application/vnd.ms-powerpoint.addin.macroEnabled.12": [".ppam"],
    "application/vnd.ms-powerpoint.slideshow.macroEnabled.12": [".ppsm"],
    "application/vnd.ms-powerpoint.template.macroEnabled.12": [".potm"],
    "application/vnd.ms-word.template.macroEnabled.12": [".dotm"],
    "application/vnd.ms-word.document.macroEnabled.12": [".docm"],
    "application/vnd.ms-word.document": [".doc"],
    "application/vnd.ms-works": [".wps"],
    "application/vnd.ms-works.word": [".wps"],
    "application/vnd.ms-works.excel": [".xlw"],
    "application/vnd.ms-works.database": [".wdb"],
    "application/vnd.ms-works.chart": [".wks"],
    "application/vnd.ms-works.word": [".wps"],
    "application/vnd.ms-works.presentation": [".wpp"],
    "application/vnd.ms-works.spreadsheet": [".wks"],
    "application/vnd.ms-works.template": [".wpt"]
}


def get_mime_type(file_content: bytes) -> str:
    """
    Detecta o tipo MIME com base no conteúdo do arquivo.
    """
    mime = magic.Magic(mime=True)
    return mime.from_buffer(file_content)

def get_extension(file_path: str) -> str:
    import os
    _, ext = os.path.splitext(file_path)
    return ext.lower()

def validate_mime(file_path: str, file_content: bytes) -> bool:
    """
    Valida se o tipo MIME do conteúdo corresponde à extensão do arquivo.
    """
    mime_type = get_mime_type(file_content)
    extension = get_extension(file_path)

    return mime_type in MIME_MAPPING and extension in MIME_MAPPING[mime_type]
