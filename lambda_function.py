import json
import base64
from base64 import b64decode
from reportlab.lib import colors
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER,TA_LEFT,TA_RIGHT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle
from reportlab.platypus.flowables import Image, PageBreak

def lambda_handler(event, context):
    # TODO implement
    date=event.get('date')
    coverdate='DATE:'+'&nbsp;'+'&nbsp;'+date
    tfno=event.get('tfno')
    Header1=event.get('header')
    filename='/tmp/'+tfno+'.pdf'
    my_colour_ligt_gray = [0.8, 0.8, 0.8]
    doc = SimpleDocTemplate(filename, pagesize=letter,rightMargin=25, leftMargin=25,topMargin=5,bottomMargin=0)
    pdfmetrics.registerFont(TTFont('English', "TTHoves-Medium.ttf"))
    Story = []
    styles = getSampleStyleSheet()
    f = open('logo.JPG', 'rb')
    Story.append(Image(f,180,80,hAlign="RIGHT"))
    
    Header = f"""<b> {Header1} </b>"""
    text = Header
    style_right = ParagraphStyle(name='left', parent=styles['Normal'], alignment=TA_CENTER,fontSize=8,fontName="English")
    para = Paragraph(text, style=style_right)
    Story.append(para)
    Story.append(Spacer(1, 5))
    text = coverdate
    style_right = ParagraphStyle(name='left', parent=styles['Normal'], alignment=TA_LEFT,fontSize=8,fontName="English")
    para = Paragraph(text, style=style_right)
    Story.append(para)
    Story.append(Spacer(1, 5))
    addrs=event.get('addrs')
    adr=f'{addrs[0]}\n{addrs[1]}\n{addrs[2]}\n{addrs[3]}'
    ref="OUR REFERENCE: "+tfno+"\n(PLEASE QUOTE IN YOUR CORRESPONDENCE)"
    TABLE_DATA2 = ((adr,ref),)
    table = Table(TABLE_DATA2, colWidths=[10 * cm,10 * cm, 4 * cm,5* cm,  5* cm],hAlign='LEFT')
    table.setStyle(TableStyle([
                       ('INNERGRID', (0,0), (-1,-1), 0.30, colors.black),
                       ('BOX', (0,0), (-1,-1), 0.30, colors.black),
                       ('VALIGN',(0,0),(-1, -1),'TOP'),
                       ('ALIGN', (0, 0), (-1, -1), "CENTER"),
                       ('FONTSIZE', (0,0), (-1,-1), 7),
                       ('FONTNAME ', (0,0), (-1,-1), "English"),
                       ('BACKGROUND', (2,0 ), (0, 2), my_colour_ligt_gray),
                       #('SPAN',(0,0),(0,0)),
                       #('SPAN',(0,7),(0,4))

                       ]))
    Story.append(table)
    Story.append(Spacer(1, 3))
    para1="DEAR SIR,"
    para2="WE ENCLOSE THE FOLLOWING DOCUMENTS NEGOTIATED BY US AS PER L/C TERMS."
    text = para1
    style_right = ParagraphStyle(name='left', parent=styles['Normal'], alignment=TA_LEFT,fontSize=8,fontName="English")
    para = Paragraph(text, style=style_right)
    Story.append(para)
    text = para2
    style_right = ParagraphStyle(name='left', parent=styles['Normal'], alignment=TA_LEFT,fontSize=8,fontName="English")
    para = Paragraph(text, style=style_right)
    Story.append(para)
    Story.append(Spacer(1, 3))
    lcissue1=event.get('issuingbank')
    lcissue2=event.get('issingbankref')
    lcissue1addr=f'{lcissue1[1]}\n{lcissue1[2]}\n{lcissue1[3]}'
    TABLE_DATA2 = ((lcissue1[0],lcissue2[0]),(lcissue1addr,lcissue2[1]),)
    table = Table(TABLE_DATA2, colWidths=[10 * cm,10 * cm, 2 * cm,2* cm,  2* cm],hAlign='LEFT')
    table.setStyle(TableStyle([
                       ('INNERGRID', (0,0), (-1,-1), 0.30, colors.black),
                       ('BOX', (0,0), (-1,-1), 0.30, colors.black),
                       ('VALIGN',(0,0),(-1, -1),'TOP'),
                       ('ALIGN', (0, 0), (-1, -1), "CENTER"),
                       ('FONTSIZE', (0,0), (-1,-1), 7),
                       ('FONTNAME ', (0,0), (-1,-1), "English"),
                       ('BACKGROUND', (0, 0), (1, 0), my_colour_ligt_gray),
                       #('SPAN',(0,0),(0,4)),
                       #('SPAN',(0,7),(0,4))

                       ]))
    Story.append(table)
    Story.append(Spacer(1, 5))
    #applicantaddrs=event.get('applicantaddrs')
    
    #benaddrs=event.get('benaddrs')
    #appladdrs=f'{applicantaddrs[0]}\n{applicantaddrs[1]}\n{applicantaddrs[2]}\n{applicantaddrs[3]}'
    #bnddrs=f'{benaddrs[0]}\n{benaddrs[1]}\n{benaddrs[2]}\n{benaddrs[3]}'
    #TABLE_DATA2 = (("APPLICANT","BENEFICIARY"),(appladdrs,bnddrs),)
    #table = Table(TABLE_DATA2, colWidths=[10 * cm,10 * cm, 4 * cm,5* cm,  5* cm],hAlign='LEFT')
    #table.setStyle(TableStyle([
    #                   ('INNERGRID', (0,0), (-1,-1), 0.30, colors.black),
    #                   ('BOX', (0,0), (-1,-1), 0.30, colors.black),
    #                   ('VALIGN',(0,0),(-1, -1),'TOP'),
    #                   ('ALIGN', (0, 0), (-1, -1), "CENTER"),
    #                   ('FONTSIZE', (0,0), (-1,-1), 9),
    #                  ('FONTNAME ', (0,0), (-1,-1), "English"),
    #                   ('BACKGROUND', (0,0 ), (1, 0), my_colour_ligt_gray),
    #                   ('SPAN',(0,0),(0,0)),
    #                   #('SPAN',(0,7),(0,4))

    #                   ]))
    #Story.append(table)
    #Story.append(Spacer(1, 5))
    tnr1=event.get('tnr1')
    tnr2=event.get('tnr2')
    tnr3=event.get('tnr3')
    tenordata12=f'{tnr1}\n{tnr2}\n{tnr3}'
    print(tenordata12)
    tnrdata=[tenordata12,"","",""]
    tenordata2=event.get('tenordata2')
    tenordata3=event.get('tenordata3')
    #adr=f'{addrs[0]}\n{addrs[1]}\n{addrs[2]}\n{addrs[3]}'
    zipped=[list(t) for t in zip(tnrdata,tenordata2,tenordata3)]
    data =zipped
    table = Table(data, colWidths=[6.8 * cm,6.4 * cm,6.8 * cm,4 * cm,4* cm],hAlign='LEFT')
    table.setStyle(TableStyle([
                       ('INNERGRID', (0,0), (-1,-1), 0.30, colors.black),
                       ('BOX', (0,0), (-1,-1), 0.30, colors.black),
                       ('VALIGN',(0,0),(-1, -1),'TOP'),
                       ('ALIGN', (0, 0), (-1, -1), "LEFT"),
                       ('FONTSIZE', (0,0), (-1,-1), 7),
                       ('fontName', (0,0), (-1,-1), "English"),
                       ('SPAN',(0,0),(0,3))
                       #('SPAN',(0,7),(0,4))
                       #('BACKGROUND', (0, 0), (0, 7), my_colour_ligt_gray)
                       ]))
    Story.append(table)
    Story.append(Spacer(1, 5))
    encloseddoc1=event.get('encloseddoc1')
    
    encloseddoc2=event.get('encloseddoc2')
    zipped = [list(t) for t in zip(encloseddoc1, encloseddoc2)]
    data =zipped   
    #docenclosed=event.get(data)
    table = Table(data, colWidths=[10 * cm,10 * cm, 4 * cm,5* cm,  5* cm],hAlign='LEFT')
    table.setStyle(TableStyle([
                       ('INNERGRID', (0,0), (-1,-1), 0.30, colors.black),
                       ('BOX', (0,0), (-1,-1), 0.30, colors.black),
                       ('VALIGN',(0,0),(-1, -1),'TOP'),
                       ('ALIGN', (0, 0), (-1, -1), "LEFT"),
                       ('FONTSIZE', (0,0), (-1,-1), 7),
                       ('fontName', (0,0), (-1,-1), "English"),
                       ('BACKGROUND', (0, 0), (1, 0), my_colour_ligt_gray)
                       ]))
    Story.append(table)
    Story.append(Spacer(1, 5))
    #goodsdata=event.get('goodsdata')
    #table = Table(goodsdata, colWidths=[10 * cm,10 * cm, 4 * cm,5* cm,  5* cm],hAlign='LEFT')
    #table.setStyle(TableStyle([
    #                   ('INNERGRID', (0,0), (-1,-1), 0.30, colors.black),
    #                   ('BOX', (0,0), (-1,-1), 0.30, colors.black),
    #                   ('VALIGN',(0,0),(-1, -1),'TOP'),
    #                   ('ALIGN', (0, 0), (-1, -1), "LEFT"),
    #                   ('FONTSIZE', (0,0), (-1,-1), 9),
    #                   ('fontName', (0,0), (-1,-1), "English"),
    #                   ('BACKGROUND', (0, 0), (1, 0), my_colour_ligt_gray)
    #                   ]))
    #Story.append(table)
    #Story.append(Spacer(1, 5))
    para3="<u>PAYMENT INSTRUCTION/DETAILS:</u>"
    text = para3
    style_right = ParagraphStyle(name='left', parent=styles['Normal'], alignment=TA_LEFT,fontSize=8,fontName="English")
    para = Paragraph(text, style=style_right)
    Story.append(para)
    Story.append(Spacer(1, 5))
    para4=event.get('paymentinstruction1')
    text = para4
    style_right = ParagraphStyle(name='left', parent=styles['Normal'], alignment=TA_JUSTIFY,fontSize=8,fontName="English")
    para = Paragraph(text, style=style_right)
    Story.append(para)
    Story.append(Spacer(1, 5))
    para5=event.get('paymentinstruction2')
    text = para5
    style_right = ParagraphStyle(name='left', parent=styles['Normal'], alignment=TA_LEFT,fontSize=8,fontName="English")
    para = Paragraph(text, style=style_right)
    Story.append(para)
    Story.append(Spacer(1, 10))
    f = open('STAMP.png', 'rb')
    Story.append(Image(f,hAlign="RIGHT"))
    para6="FOR AL SALAM BANK B.S.C."
    text = para6
    style_right = ParagraphStyle(name='left', parent=styles['Normal'], alignment=TA_LEFT,fontSize=8,fontName="English")
    para = Paragraph(text, style=style_right)
    Story.append(para)
    #Story.append(Spacer(1, 10))
    para7="TRADE FINANCE OPS"
    text = para7
    style_right = ParagraphStyle(name='left', parent=styles['Normal'], alignment=TA_LEFT,fontSize=8,fontName="English")
    para = Paragraph(text, style=style_right)
    Story.append(para)
    Story.append(Spacer(1, 5))
    para8=[["PRESENTATION IS UNDERTAKEN SUBJECT TO UNIFORM CUSTOMS AND PRACTICES FOR DOCUMENTARY CREDITS, \n2007 REVISION, ICC PUBLICATION NO.600"]]
    table = Table(para8, colWidths=[20 * cm,40* cm],hAlign='LEFT')
    table.setStyle(TableStyle([
                       ('INNERGRID', (0,0), (-1,-1), 0.30, colors.black),
                       ('BOX', (0,0), (-1,-1), 0.30, colors.black),
                       ('VALIGN',(0,0),(-1, -1),'TOP'),
                       ('ALIGN', (0, 0), (-1, -1), "LEFT"),
                       ('FONTSIZE', (0,0), (-1,-1), 7),
                       ('fontName', (0,0), (-1,-1), "English"),
                       ('BACKGROUND', (0, 0), (1, 0), my_colour_ligt_gray)
                       ]))
    Story.append(table)
    Story.append(Spacer(1, 10))
    parasig="THIS IS A COMPUTER GENERATED ADVICE THAT REQUIRES NO SIGNATURE"
    text = parasig
    style_right = ParagraphStyle(name='left', parent=styles['Normal'], alignment=TA_LEFT,fontSize=8,fontName="English")
    para = Paragraph(text, style=style_right)
    Story.append(para)
    encldoclen=len(encloseddoc1)
    #if encldoclen<8:
    Story.append(Spacer(1, 10))
    #else:
    
    footer=["AL SALAM BANK B.S.C., ","P.O. BOX 18282, "," MANAMA, KINGDOM OF BAHRAIN, ","TEL: +973 1700 5500, ","www.alsalambank.com"]
    text = footer[0]+footer[1]+footer[2]+footer[3]
    style_right = ParagraphStyle(name='left', parent=styles['Normal'], alignment=TA_CENTER,fontSize=8,fontName="English")
    para = Paragraph(text, style=style_right)
    Story.append(para)
    doc.build(Story)
    with open(filename, "rb") as pdf_file:
        encoded_string = base64.b64encode(pdf_file.read())
        base64_message = encoded_string.decode('utf-8')
    return {
        'statusCode': 200,
        'body': base64_message
    } 