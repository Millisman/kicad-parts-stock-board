import uuid

data = [
["CL05A225MQ5NSNC","C12530","B","6.3V","2.2uF","X5R","±20%","0402","SMD/SMT","ROHS","Samsung Electro-Mechanics","https://datasheet.lcsc.com/lcsc/1811021410_Samsung-Electro-Mechanics-CL05A225MQ5NSNC_C12530.pdf"],
["CL05C331JB5NNNC","C13533","B","50V","330pF","C0G","±5%","0402","SMD/SMT","ROHS","Samsung Electro-Mechanics","https://datasheet.lcsc.com/lcsc/1810192025_Samsung-Electro-Mechanics-CL05C331JB5NNNC_C13533.pdf"],
["CL05C680JB5NNNC","C14441","B","50V","68pF","C0G","±5%","0402","SMD/SMT","ROHS","Samsung Electro-Mechanics","https://datasheet.lcsc.com/lcsc/1810191215_Samsung-Electro-Mechanics-CL05C680JB5NNNC_C14441.pdf"],
["CL05B103KB5NNNC","C15195","B","50V","10nF","X7R","±10%","0402","SMD/SMT","ROHS","Samsung Electro-Mechanics","https://datasheet.lcsc.com/lcsc/1810191223_Samsung-Electro-Mechanics-CL05B103KB5NNNC_C15195.pdf"],
["0402B102K500NT","C1523","B","50V","1nF","X7R","±10%","0402","SMD/SMT","ROHS","FH (Guangdong Fenghua Advanced Tech)","https://datasheet.lcsc.com/lcsc/1809291524_FH--Guangdong-Fenghua-Advanced-Tech-0402B102K500NT_C1523.pdf"],
["CL05B104KO5NNNC","C1525","B","16V","100nF","X7R","±10%","0402","SMD/SMT","ROHS","Samsung Electro-Mechanics","https://datasheet.lcsc.com/lcsc/1810191219_Samsung-Electro-Mechanics-CL05B104KO5NNNC_C1525.pdf"],
["0402B151K500NT","C1527","B","50V","150pF","X7R","±10%","0402","SMD/SMT","ROHS","FH (Guangdong Fenghua Advanced Tech)","https://datasheet.lcsc.com/lcsc/1810302110_FH--Guangdong-Fenghua-Advanced-Tech-0402B151K500NT_C1527.pdf"],
["0402B221K500NT","C1530","B","50V","220pF","X7R","±10%","0402","SMD/SMT","ROHS","FH (Guangdong Fenghua Advanced Tech)","https://datasheet.lcsc.com/lcsc/1811151132_FH--Guangdong-Fenghua-Advanced-Tech-0402B221K500NT_C1530.pdf"],
["0402B222K500NT","C1531","B","50V","2.2nF","X7R","±10%","0402","SMD/SMT","ROHS","FH (Guangdong Fenghua Advanced Tech)","https://datasheet.lcsc.com/lcsc/1811141710_FH--Guangdong-Fenghua-Advanced-Tech-0402B222K500NT_C1531.pdf"],
["0402B223K500NT","C1532","B","50V","22nF","X7R","±10%","0402","SMD/SMT","ROHS","FH (Guangdong Fenghua Advanced Tech)","https://datasheet.lcsc.com/lcsc/1811141710_FH--Guangdong-Fenghua-Advanced-Tech-0402B223K500NT_C1532.pdf"],
["0402B471K500NT","C1537","B","50V","470pF","X7R","±10%","0402","SMD/SMT","ROHS","FH (Guangdong Fenghua Advanced Tech)","https://datasheet.lcsc.com/lcsc/1811141710_FH--Guangdong-Fenghua-Advanced-Tech-0402B471K500NT_C1537.pdf"],
["0402B472K500NT","C1538","B","50V","4.7nF","X7R","±10%","0402","SMD/SMT","ROHS","FH (Guangdong Fenghua Advanced Tech)","https://datasheet.lcsc.com/lcsc/1811031110_FH--Guangdong-Fenghua-Advanced-Tech-0402B472K500NT_C1538.pdf"],
["0402B682K500NT","C1542","B","50V","6.8nF","X7R","±10%","0402","SMD/SMT","ROHS","FH (Guangdong Fenghua Advanced Tech)","https://datasheet.lcsc.com/lcsc/1811141710_FH--Guangdong-Fenghua-Advanced-Tech-0402B682K500NT_C1542.pdf"],
["0402CG101J500NT","C1546","B","50V","100pF","C0G","±5%","0402","SMD/SMT","ROHS","FH (Guangdong Fenghua Advanced Tech)","https://datasheet.lcsc.com/lcsc/1810151218_FH--Guangdong-Fenghua-Advanced-Tech-0402CG101J500NT_C1546.pdf"],
["0402CG120J500NT","C1547","B","50V","12pF","C0G","±5%","0402","SMD/SMT","ROHS","FH (Guangdong Fenghua Advanced Tech)","https://datasheet.lcsc.com/lcsc/1811141710_FH--Guangdong-Fenghua-Advanced-Tech-0402CG120J500NT_C1547.pdf"],
["0402CG150J500NT","C1548","B","50V","15pF","C0G","±5%","0402","SMD/SMT","ROHS","FH (Guangdong Fenghua Advanced Tech)","https://datasheet.lcsc.com/lcsc/1810111610_FH--Guangdong-Fenghua-Advanced-Tech-0402CG150J500NT_C1548.pdf"],
["0402CG180J500NT","C1549","B","50V","18pF","C0G","±5%","0402","SMD/SMT","ROHS","FH (Guangdong Fenghua Advanced Tech)","https://datasheet.lcsc.com/lcsc/1811141814_FH--Guangdong-Fenghua-Advanced-Tech-0402CG180J500NT_C1549.pdf"],
["0402CG1R0C500NT","C1550","B","50V","1pF","C0G","±5%","0402","SMD/SMT","ROHS","FH (Guangdong Fenghua Advanced Tech)","https://datasheet.lcsc.com/lcsc/1811141710_FH--Guangdong-Fenghua-Advanced-Tech-0402CG1R0C500NT_C1550.pdf"],
["0402CG1R5C500NT","C1552","B","50V","1.5pF","C0G","±5%","0402","SMD/SMT","ROHS","FH (Guangdong Fenghua Advanced Tech)","https://datasheet.lcsc.com/lcsc/1811151132_FH--Guangdong-Fenghua-Advanced-Tech-0402CG1R5C500NT_C1552.pdf"],
["CL05A106MQ5NUNC","C15525","B","6.3V","10uF","X5R","±20%","0402","SMD/SMT","ROHS","Samsung Electro-Mechanics","https://datasheet.lcsc.com/lcsc/2208231630_Samsung-Electro-Mechanics-CL05A106MQ5NUNC_C15525.pdf"],
["0402CG200J500NT","C1554","B","50V","20pF","C0G","±5%","0402","SMD/SMT","ROHS","FH (Guangdong Fenghua Advanced Tech)","https://datasheet.lcsc.com/lcsc/1811141710_FH--Guangdong-Fenghua-Advanced-Tech-0402CG200J500NT_C1554.pdf"],
["0402CG220J500NT","C1555","B","50V","22pF","C0G","±5%","0402","SMD/SMT","ROHS","FH (Guangdong Fenghua Advanced Tech)","https://datasheet.lcsc.com/lcsc/1811141710_FH--Guangdong-Fenghua-Advanced-Tech-0402CG220J500NT_C1555.pdf"],
["0402CG270J500NT","C1557","B","50V","27pF","C0G","±5%","0402","SMD/SMT","ROHS","FH (Guangdong Fenghua Advanced Tech)","https://datasheet.lcsc.com/lcsc/1811141710_FH--Guangdong-Fenghua-Advanced-Tech-0402CG270J500NT_C1557.pdf"],
["0402CG2R2C500NT","C1559","B","50V","2.2pF","C0G","±5%","0402","SMD/SMT","ROHS","FH (Guangdong Fenghua Advanced Tech)","https://datasheet.lcsc.com/lcsc/1811141843_FH--Guangdong-Fenghua-Advanced-Tech-0402CG2R2C500NT_C1559.pdf"],
["0402CG2R7C500NT","C1561","B","50V","2.7pF","C0G","±5%","0402","SMD/SMT","ROHS","FH (Guangdong Fenghua Advanced Tech)","https://datasheet.lcsc.com/lcsc/1811141710_FH--Guangdong-Fenghua-Advanced-Tech-0402CG2R7C500NT_C1561.pdf"],
["0402CG330J500NT","C1562","B","50V","33pF","C0G","±5%","0402","SMD/SMT","ROHS","FH (Guangdong Fenghua Advanced Tech)","https://datasheet.lcsc.com/lcsc/1811141731_FH--Guangdong-Fenghua-Advanced-Tech-0402CG330J500NT_C1562.pdf"],
["0402CG3R3C500NT","C1565","B","50V","3.3pF","C0G","±5%","0402","SMD/SMT","ROHS","FH (Guangdong Fenghua Advanced Tech)","https://datasheet.lcsc.com/lcsc/1811141710_FH--Guangdong-Fenghua-Advanced-Tech-0402CG3R3C500NT_C1565.pdf"],
["0402CG470J500NT","C1567","B","50V","47pF","C0G","±5%","0402","SMD/SMT","ROHS","FH (Guangdong Fenghua Advanced Tech)","https://datasheet.lcsc.com/lcsc/1811151132_FH--Guangdong-Fenghua-Advanced-Tech-0402CG470J500NT_C1567.pdf"],
["0402CG4R7C500NT","C1569","B","50V","4.7pF","C0G","±5%","0402","SMD/SMT","ROHS","FH (Guangdong Fenghua Advanced Tech)","https://datasheet.lcsc.com/lcsc/1811141710_FH--Guangdong-Fenghua-Advanced-Tech-0402CG4R7C500NT_C1569.pdf"],
["0402CG300J500NT","C1570","B","50V","30pF","C0G","±5%","0402","SMD/SMT","ROHS","FH (Guangdong Fenghua Advanced Tech)","https://datasheet.lcsc.com/lcsc/1811141710_FH--Guangdong-Fenghua-Advanced-Tech-0402CG300J500NT_C1570.pdf"],
["0402CG6R8C500NT","C1576","B","50V","6.8pF","C0G","±5%","0402","SMD/SMT","ROHS","FH (Guangdong Fenghua Advanced Tech)","https://datasheet.lcsc.com/lcsc/1811141710_FH--Guangdong-Fenghua-Advanced-Tech-0402CG6R8C500NT_C1576.pdf"],
["C1585","C1585","B","50V","33nF","Y5V","±20%","0402","SMD/SMT","ROHS","FH (Guangdong Fenghua Advanced Tech)","https://datasheet.lcsc.com/lcsc/1811141711_FH--Guangdong-Fenghua-Advanced-Tech-0402F333M500NT--SMT----_C1585.pdf"],
["CL05B224KO5NNNC","C16772","B","16V","220nF","X7R","±10%","0402","SMD/SMT","ROHS","Samsung Electro-Mechanics","https://datasheet.lcsc.com/lcsc/1810251021_Samsung-Electro-Mechanics-CL05B224KO5NNNC-_C16772.pdf"],
["CL05A475MP5NRNC","C23733","B","10V","4.7uF","X5R","±20%","0402","SMD/SMT","ROHS","Samsung Electro-Mechanics","https://datasheet.lcsc.com/lcsc/1810191211_Samsung-Electro-Mechanics-CL05A475MP5NRNC_C23733.pdf"],
["CL05B332KB5NNNC","C26404","B","50V","3.3nF","X7R","±10%","0402","SMD/SMT","ROHS","Samsung Electro-Mechanics","https://datasheet.lcsc.com/lcsc/1810191211_Samsung-Electro-Mechanics-CL05B332KB5NNNC_C26404.pdf"],
["CL05B104KB54PNC","C307331","B","50V","100nF","X7R","±10%","0402","SMD/SMT","ROHS","Samsung Electro-Mechanics","https://datasheet.lcsc.com/lcsc/1810191222_Samsung-Electro-Mechanics-CL05B104KB54PNC_C307331.pdf"],
["CL05C100JB5NNNC","C32949","B","50V","10pF","C0G","±5%","0402","SMD/SMT","ROHS","Samsung Electro-Mechanics","https://datasheet.lcsc.com/lcsc/1810191220_Samsung-Electro-Mechanics-CL05C100JB5NNNC_C32949.pdf"],
["CL05A474KP5NNNC","C47339","B","10V","470nF","X5R","±10%","0402","SMD/SMT","ROHS","Samsung Electro-Mechanics","https://datasheet.lcsc.com/lcsc/1810191214_Samsung-Electro-Mechanics-CL05A474KP5NNNC-_C47339.pdf"],
["CL05A105KA5NQNC","C52923","B","25V","1uF","X5R","±10%","0402","SMD/SMT","ROHS","Samsung Electro-Mechanics","https://datasheet.lcsc.com/lcsc/1811091611_Samsung-Electro-Mechanics-CL05A105KA5NQNC_C52923.pdf"],
]

print ("""
(lib_symbols
  (symbol "Device:C_Small" (pin_numbers hide) (pin_names (offset 0.254) hide) (in_bom yes) (on_board yes)
    (property "Reference" "C" (at 0.254 1.778 0)
      (effects (font (size 1.27 1.27)) (justify left))
    )
    (property "Value" "C_Small" (at 0.254 -2.032 0)
      (effects (font (size 1.27 1.27)) (justify left))
    )
    (property "Footprint" "" (at 0 0 0)
      (effects (font (size 1.27 1.27)) hide)
    )
    (property "Datasheet" "~" (at 0 0 0)
      (effects (font (size 1.27 1.27)) hide)
    )
    (property "ki_keywords" "capacitor cap" (at 0 0 0)
      (effects (font (size 1.27 1.27)) hide)
    )
    (property "ki_description" "Unpolarized capacitor, small symbol" (at 0 0 0)
      (effects (font (size 1.27 1.27)) hide)
    )
    (property "ki_fp_filters" "C_*" (at 0 0 0)
      (effects (font (size 1.27 1.27)) hide)
    )
    (symbol "C_Small_0_1"
      (polyline
        (pts
          (xy -1.524 -0.508)
          (xy 1.524 -0.508)
        )
        (stroke (width 0.3302) (type default))
        (fill (type none))
      )
      (polyline
        (pts
          (xy -1.524 0.508)
          (xy 1.524 0.508)
        )
        (stroke (width 0.3048) (type default))
        (fill (type none))
      )
    )
    (symbol "C_Small_1_1"
      (pin passive line (at 0 2.54 270) (length 2.032)
        (name "~" (effects (font (size 1.27 1.27))))
        (number "1" (effects (font (size 1.27 1.27))))
      )
      (pin passive line (at 0 -2.54 90) (length 2.032)
        (name "~" (effects (font (size 1.27 1.27))))
        (number "2" (effects (font (size 1.27 1.27))))
      )
    )
  )
)""")

#num = 0
#for x in data:
  #print(x)
  #print(num)
  #num+=1


#0 "CL05A105KA5NQNC"
#1 "C52923"
#2 "B"
#3 "25V"
#4 "1uF"
#5 "X5R"
#6 "±10%"
#7 "0402"
#8 "SMD/SMT"
#9 "ROHS"
#10 "Samsung Electro-Mechanics"
#11 "https://datasheet.lcsc.com/lcsc/1811091611_Samsung-Electro-Mechanics-CL05A105KA5NQNC_C52923.pdf"

  #(property "Reference" "C24" (at 54.61 35.56 90)
    #(effects (font (size 1.27 1.27)) (justify left))
  #)

n = 0
v1 = 60.96
v2 = 38.1
v3 = 63.5
v4 = 35.56
v5 = 69.85
v6 = 40.64
v7 = 57.15
v8 = 54.61
step = 5.08
for x in data:

    v1 += step
    v2 += step
    v3 += step
    v4 += step
    v5 += step
    v6 += step
    v7 += step
    v8 += step
    #print(x)
    #print(num)
    #num+=1
    #(uuid """ + str(uuid.uuid4()) + """)
    print ("""
(symbol (lib_id "Device:C_Small") (at """ + str(v1) + """ """ + str(v2) + """ 90) (unit 1)
  (in_bom yes) (on_board yes) (dnp no)

  (property "Reference" "C" (at """ + str(v8) + """ """ + str(v4) + """ 90)
    (effects (font (size 1.27 1.27)) (justify left))
  )
  (property "Value" """ + '"' + x[4] + '"' + """ (at """ + str(v3) + """ """ + str(v4) + """ 90)
    (effects (font (size 1.27 1.27)) (justify left))
  )
  (property "Footprint" "Capacitor_SMD:C_0402_1005Metric" (at """ + str(v1) + """ """ + str(v2) + """ 0)
    (effects (font (size 1.27 1.27)) hide)
  )
  (property "Datasheet" """ + '"' + x[11] + '"' + """ (at """ + str(v1) + """ """ + str(v2) + """ 0)
    (effects (font (size 1.27 1.27)) hide)
  )
  (property "LCSC" """ + '"' + x[1] + '"' + """ (at """ + str(v1) + """ """ + str(v2) + """ 0)
    (effects (font (size 1.27 1.27)) hide)
  )
  (property "Manufacturer Part" """ + '"' + x[0] + '"' + """ (at """ + str(v1) + """ """ + str(v2) + """ 0)
    (effects (font (size 1.27 1.27)) hide)
  )
  (property "Tolerance" """ + '"' + x[6] + '"' + """ (at """ + str(v3) + """ """ + str(v4) + """ 90)
    (effects (font (size 1.27 1.27)) (justify right))
  )
  (property "Voltage Rated" """ + '"' + x[3] + '"' + """ (at """ + str(v5) + """ """ + str(v4) + """ 90)
    (effects (font (size 1.27 1.27)) (justify right))
  )
  (property "Dielectric" """ + '"' + x[5] + '"' + """ (at """ + str(v3) + """ """ + str(v6) + """ 90)
    (effects (font (size 1.27 1.27)) (justify right))
  )
  (property "Manufacturer" """ + '"' + x[10] + '"' + """ (at """ + str(v1) + """ """ + str(v2) + """ 0)
    (effects (font (size 1.27 1.27)) hide)
  )
  (property "Supplier Footprint" """ + '"' + x[7] + '"' + """ (at """ + str(v7) + """ """ + str(v6) + """ 90)
    (effects (font (size 1.27 1.27)))
  )
  (pin "1" (uuid """ + str(uuid.uuid4()) + """))
  (pin "2" (uuid """ + str(uuid.uuid4()) + """))
)
""")
