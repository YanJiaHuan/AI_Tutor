# pip install pypandoc
# from pypandoc.pandoc_download import download_pandoc
# download_pandoc()
import pypandoc

output = pypandoc.convert_file('./test/test.md', 'pptx', outputfile="./test/test.pptx")