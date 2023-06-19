import uuid

data = [
["CC0603JRNPO9BN270","C107045","B","50V","27pF","NP0","±5%","0603","SMD/SMT","ROHS","YAGEO","https://datasheet.lcsc.com/lcsc/1811082127_YAGEO-CC0603JRNPO9BN270_C107045.pdf","190804","0.003$/unit0.003$/1 units"],
["CC0603KRX7R9BB104","C14663","B","50V","100nF","X7R","±10%","0603","SMD/SMT","ROHS","YAGEO","https://datasheet.lcsc.com/lcsc/2211101700_YAGEO-CC0603KRX7R9BB104_C14663.pdf","24088251","0.002$/unit0.002$/1 units"],
["CL10C101JB8NNNC","C14858","B","50V","100pF","C0G","±5%","0603","SMD/SMT","ROHS","Samsung Electro-Mechanics","https://datasheet.lcsc.com/lcsc/1811151136_Samsung-Electro-Mechanics-CL10C101JB8NNNC_C14858.pdf","1350867","0.004$/unit0.004$/1 units"],
["CL10A105KB8NNNC","C15849","B","50V","1uF","X5R","±10%","0603","SMD/SMT","ROHS","Samsung Electro-Mechanics","https://datasheet.lcsc.com/lcsc/1810261812_Samsung-Electro-Mechanics-CL10A105KB8NNNC_C15849.pdf","5349163","0.005$/unit0.005$/1 units"],
["CL10B102KB8NNNC","C1588","B","50V","1nF","X7R","±10%","0603","SMD/SMT","ROHS","Samsung Electro-Mechanics","https://datasheet.lcsc.com/lcsc/1811071810_Samsung-Electro-Mechanics-CL10B102KB8NNNC_C1588.pdf","2823376","0.003$/unit0.003$/1 units"],
["0603B151K500NT","C1594","B","50V","150pF","X7R","±10%","0603","SMD/SMT","ROHS","FH (Guangdong Fenghua Advanced Tech)","https://datasheet.lcsc.com/lcsc/1811061810_FH--Guangdong-Fenghua-Advanced-Tech-0603B151K500NT_C1594.pdf","143226","0.003$/unit0.003$/1 units"],
["0603B152K500NT","C1595","B","50V","1.5nF","X7R","±10%","0603","SMD/SMT","ROHS","FH (Guangdong Fenghua Advanced Tech)","https://datasheet.lcsc.com/lcsc/1811061810_FH--Guangdong-Fenghua-Advanced-Tech-0603B152K500NT_C1595.pdf","2462963","0.003$/unit0.003$/1 units"],
["0603B153K500NT","C1596","B","50V","15nF","X7R","±10%","0603","SMD/SMT","ROHS","FH (Guangdong Fenghua Advanced Tech)","https://datasheet.lcsc.com/lcsc/1811061810_FH--Guangdong-Fenghua-Advanced-Tech-0603B153K500NT_C1596.pdf","87224","0.004$/unit0.004$/1 units"],
["0603B201K500NT","C1600","B","50V","200pF","X7R","±10%","0603","SMD/SMT","ROHS","FH (Guangdong Fenghua Advanced Tech)","https://datasheet.lcsc.com/lcsc/1811061810_FH--Guangdong-Fenghua-Advanced-Tech-0603B201K500NT_C1600.pdf","30143","0.003$/unit0.003$/1 units"],
["CL10B221KB8NNNC","C1603","B","50V","220pF","X7R","±10%","0603","SMD/SMT","ROHS","Samsung Electro-Mechanics","https://datasheet.lcsc.com/lcsc/1810261515_Samsung-Electro-Mechanics-CL10B221KB8NNNC_C1603.pdf","205741","0.005$/unit0.005$/1 units"],
["0603B222K500NT","C1604","B","50V","2.2nF","X7R","±10%","0603","SMD/SMT","ROHS","FH (Guangdong Fenghua Advanced Tech)","https://datasheet.lcsc.com/lcsc/1810301614_FH--Guangdong-Fenghua-Advanced-Tech-0603B222K500NT_C1604.pdf","333682","0.002$/unit0.002$/1 units"],
["0603B272K500NT","C1609","B","50V","2.7nF","X7R","±10%","0603","SMD/SMT","ROHS","FH (Guangdong Fenghua Advanced Tech)","https://datasheet.lcsc.com/lcsc/1811151136_FH--Guangdong-Fenghua-Advanced-Tech-0603B272K500NT_C1609.pdf","27098","0.002$/unit0.002$/1 units"],
["CL10B332KB8NNNC","C1613","B","50V","3.3nF","X7R","±10%","0603","SMD/SMT","ROHS","Samsung Electro-Mechanics","https://datasheet.lcsc.com/lcsc/1810261513_Samsung-Electro-Mechanics-CL10B332KB8NNNC_C1613.pdf","119456","0.007$/unit0.007$/1 units"],
["0603B334K250NT","C1615","B","25V","330nF","X7R","±10%","0603","SMD/SMT","ROHS","FH (Guangdong Fenghua Advanced Tech)","https://datasheet.lcsc.com/lcsc/1811061811_FH--Guangdong-Fenghua-Advanced-Tech-0603B334K250NT_C1615.pdf","98598","0.01$/unit0.01$/1 units"],
["0603B471K500NT","C1620","B","50V","470pF","X7R","±10%","0603","SMD/SMT","ROHS","FH (Guangdong Fenghua Advanced Tech)","https://datasheet.lcsc.com/lcsc/1810302011_FH--Guangdong-Fenghua-Advanced-Tech-0603B471K500NT_C1620.pdf","240430","0.002$/unit0.002$/1 units"],
["CL10B473KB8NNNC","C1622","B","50V","47nF","X7R","±10%","0603","SMD/SMT","ROHS","Samsung Electro-Mechanics","https://datasheet.lcsc.com/lcsc/1810261614_Samsung-Electro-Mechanics-CL10B473KB8NNNC_C1622.pdf","390907","0.005$/unit0.005$/1 units"],
["CL10B474KA8NNNC","C1623","B","25V","470nF","X7R","±10%","0603","SMD/SMT","ROHS","Samsung Electro-Mechanics","https://datasheet.lcsc.com/lcsc/1810261513_Samsung-Electro-Mechanics-CL10B474KA8NNNC_C1623.pdf","645260","0.007$/unit0.007$/1 units"],
["0603B681K500NT","C1630","B","50V","680pF","X7R","±10%","0603","SMD/SMT","ROHS","FH (Guangdong Fenghua Advanced Tech)","https://datasheet.lcsc.com/lcsc/1811061822_FH--Guangdong-Fenghua-Advanced-Tech-0603B681K500NT_C1630.pdf","119762","0.002$/unit0.002$/1 units"],
["0603B682K500NT","C1631","B","50V","6.8nF","X7R","±10%","0603","SMD/SMT","ROHS","FH (Guangdong Fenghua Advanced Tech)","https://datasheet.lcsc.com/lcsc/1811061811_FH--Guangdong-Fenghua-Advanced-Tech-0603B682K500NT_C1631.pdf","148167","0.003$/unit0.003$/1 units"],
["CL10C100JB8NNNC","C1634","B","50V","10pF","C0G","±5%","0603","SMD/SMT","ROHS","Samsung Electro-Mechanics","https://datasheet.lcsc.com/lcsc/1810261513_Samsung-Electro-Mechanics-CL10C100JB8NNNC_C1634.pdf","360305","0.006$/unit0.006$/1 units"],
["CL10C150JB8NNNC","C1644","B","50V","15pF","C0G","±5%","0603","SMD/SMT","ROHS","Samsung Electro-Mechanics","https://datasheet.lcsc.com/lcsc/1810261515_Samsung-Electro-Mechanics-CL10C150JB8NNNC_C1644.pdf","279739","0.005$/unit0.005$/1 units"],
["CL10C180JB8NNNC","C1647","B","50V","18pF","C0G","±5%","0603","SMD/SMT","ROHS","Samsung Electro-Mechanics","https://datasheet.lcsc.com/lcsc/1810261621_Samsung-Electro-Mechanics-CL10C180JB8NNNC_C1647.pdf","153596","0.006$/unit0.006$/1 units"],
["CL10C200JB8NNNC","C1648","B","50V","20pF","C0G","±5%","0603","SMD/SMT","ROHS","Samsung Electro-Mechanics","https://datasheet.lcsc.com/lcsc/1810261514_Samsung-Electro-Mechanics-CL10C200JB8NNNC_C1648.pdf","375475","0.006$/unit0.006$/1 units"],
["CL10C220JB8NNNC","C1653","B","50V","22pF","C0G","±5%","0603","SMD/SMT","ROHS","Samsung Electro-Mechanics","https://datasheet.lcsc.com/lcsc/1810121815_Samsung-Electro-Mechanics-CL10C220JB8NNNC_C1653.pdf","832020","0.006$/unit0.006$/1 units"],
["0603CG300J500NT","C1658","B","50V","30pF","C0G","±5%","0603","SMD/SMT","ROHS","FH (Guangdong Fenghua Advanced Tech)","https://datasheet.lcsc.com/lcsc/1810261611_FH--Guangdong-Fenghua-Advanced-Tech-0603CG300J500NT_C1658.pdf","165158","0.003$/unit0.003$/1 units"],
["CL10C330JB8NNNC","C1663","B","50V","33pF","C0G","±5%","0603","SMD/SMT","ROHS","Samsung Electro-Mechanics","https://datasheet.lcsc.com/lcsc/1811151146_Samsung-Electro-Mechanics-CL10C330JB8NNNC_C1663.pdf","509494","0.006$/unit0.006$/1 units"],
["CL10C331JB8NNNC","C1664","B","50V","330pF","C0G","±5%","0603","SMD/SMT","ROHS","Samsung Electro-Mechanics","https://datasheet.lcsc.com/lcsc/1810261512_Samsung-Electro-Mechanics-CL10C331JB8NNNC_C1664.pdf","163661","0.007$/unit0.007$/1 units"],
["0603CG4R7C500NT","C1669","B","50V","4.7pF","C0G","±0.25pF","0603","SMD/SMT","ROHS","FH (Guangdong Fenghua Advanced Tech)","https://datasheet.lcsc.com/lcsc/1810261624_FH--Guangdong-Fenghua-Advanced-Tech-0603CG4R7C500NT_C1669.pdf","443761","0.003$/unit0.003$/1 units"],
["CL10C470JB8NNNC","C1671","B","50V","47pF","C0G","±5%","0603","SMD/SMT","ROHS","Samsung Electro-Mechanics","https://datasheet.lcsc.com/lcsc/1810261610_Samsung-Electro-Mechanics-CL10C470JB8NNNC_C1671.pdf","261797","0.006$/unit0.006$/1 units"],
["0603CG6R8C500NT","C1679","B","50V","6.8pF","C0G","±0.25pF","0603","SMD/SMT","ROHS","FH (Guangdong Fenghua Advanced Tech)","https://datasheet.lcsc.com/lcsc/1811061822_FH--Guangdong-Fenghua-Advanced-Tech-0603CG6R8C500NT_C1679.pdf","2362432","0.003$/unit0.003$/1 units"],
["0603CG8R2C500NT","C1685","B","50V","8.2pF","C0G","±0.25pF","0603","SMD/SMT","ROHS","FH (Guangdong Fenghua Advanced Tech)","https://datasheet.lcsc.com/lcsc/1811061811_FH--Guangdong-Fenghua-Advanced-Tech-0603CG8R2C500NT_C1685.pdf","22328","0.003$/unit0.003$/1 units"],
["CL10A475KO8NNNC","C19666","B","16V","4.7uF","X5R","±10%","0603","SMD/SMT","ROHS","Samsung Electro-Mechanics","https://datasheet.lcsc.com/lcsc/1810261514_Samsung-Electro-Mechanics-CL10A475KO8NNNC_C19666.pdf","1245699","0.01$/unit0.01$/1 units"],
["CL10A106KP8NNNC","C19702","B","10V","10uF","X5R","±10%","0603","SMD/SMT","ROHS","Samsung Electro-Mechanics","https://datasheet.lcsc.com/lcsc/1810191219_Samsung-Electro-Mechanics-CL10A106KP8NNNC_C19702.pdf","4596209","0.006$/unit0.006$/1 units"],
["CL10B333KB8NNNC","C21117","B","50V","33nF","X7R","±10%","0603","SMD/SMT","ROHS","Samsung Electro-Mechanics","https://datasheet.lcsc.com/lcsc/1810261514_Samsung-Electro-Mechanics-CL10B333KB8NNNC_C21117.pdf","335179","0.005$/unit0.005$/1 units"],
["CL10B224KA8NNNC","C21120","B","25V","220nF","X7R","±10%","0603","SMD/SMT","ROHS","Samsung Electro-Mechanics","https://datasheet.lcsc.com/lcsc/1810261513_Samsung-Electro-Mechanics-CL10B224KA8NNNC_C21120.pdf","459186","0.006$/unit0.006$/1 units"],
["CL10B223KB8NNNC","C21122","B","50V","22nF","X7R","±10%","0603","SMD/SMT","ROHS","Samsung Electro-Mechanics","https://datasheet.lcsc.com/lcsc/1811101610_Samsung-Electro-Mechanics-CL10B223KB8NNNC_C21122.pdf","408289","0.004$/unit0.004$/1 units"],
["CL10A225KO8NNNC","C23630","B","16V","2.2uF","X5R","±10%","0603","SMD/SMT","ROHS","Samsung Electro-Mechanics","https://datasheet.lcsc.com/lcsc/1810271109_Samsung-Electro-Mechanics-CL10A225KO8NNNC_C23630.pdf","1759817","0.007$/unit0.007$/1 units"],
["CL10B822KB8NNNC","C27920","B","50V","8.2nF","X7R","±10%","0603","SMD/SMT","ROHS","Samsung Electro-Mechanics","https://datasheet.lcsc.com/lcsc/1810262007_Samsung-Electro-Mechanics-CL10B822KB8NNNC_C27920.pdf","0","0.004$/unit0.004$/1 units"],
["CL10C680JB8NNNC","C28262","B","50V","68pF","C0G","±5%","0603","SMD/SMT","ROHS","Samsung Electro-Mechanics","https://datasheet.lcsc.com/lcsc/1810261521_Samsung-Electro-Mechanics-CL10C680JB8NNNC_C28262.pdf","92499","0.01$/unit0.01$/1 units"],
["CL10B683KB8NNNC","C31658","B","50V","68nF","X7R","±10%","0603","SMD/SMT","ROHS","Samsung Electro-Mechanics","https://datasheet.lcsc.com/lcsc/1811072020_Samsung-Electro-Mechanics-CL10B683KB8NNNC_C31658.pdf","41627","0.007$/unit0.007$/1 units"],
["0603CG6R0C500NT","C37474","B","50V","6pF","C0G","±0.25pF","0603","SMD/SMT","ROHS","FH (Guangdong Fenghua Advanced Tech)","https://datasheet.lcsc.com/lcsc/1811061822_FH--Guangdong-Fenghua-Advanced-Tech-0603CG6R0C500NT_C37474.pdf","37682","0.003$/unit0.003$/1 units"],
["CL10C120JB8NNNC","C38523","B","50V","12pF","C0G","±5%","0603","SMD/SMT","ROHS","Samsung Electro-Mechanics","https://datasheet.lcsc.com/lcsc/1810261515_Samsung-Electro-Mechanics-CL10C120JB8NNNC_C38523.pdf","229299","0.006$/unit0.006$/1 units"],
["CL10C560JB8NNNC","C39148","B","50V","56pF","C0G","±5%","0603","SMD/SMT","ROHS","Samsung Electro-Mechanics","https://datasheet.lcsc.com/lcsc/1810261515_Samsung-Electro-Mechanics-CL10C560JB8NNNC_C39148.pdf","14643","0.008$/unit0.008$/1 units"],
["0603CG3R0C500NT","C46219","B","50V","3pF","C0G","±0.25pF","0603","SMD/SMT","ROHS","FH (Guangdong Fenghua Advanced Tech)","https://datasheet.lcsc.com/lcsc/1811061821_FH--Guangdong-Fenghua-Advanced-Tech-0603CG3R0C500NT_C46219.pdf","2365950","0.003$/unit0.003$/1 units"],
["0603B472K500NT","C53987","B","50V","4.7nF","X7R","±10%","0603","SMD/SMT","ROHS","FH (Guangdong Fenghua Advanced Tech)","https://datasheet.lcsc.com/lcsc/1811061811_FH--Guangdong-Fenghua-Advanced-Tech-0603B472K500NT_C53987.pdf","273559","0.002$/unit0.002$/1 units"],
["0603B103K500NT","C57112","B","50V","10nF","X7R","±10%","0603","SMD/SMT","ROHS","FH (Guangdong Fenghua Advanced Tech)","https://datasheet.lcsc.com/lcsc/2102081402_FH--Guangdong-Fenghua-Advanced-Tech-0603B103K500NT_C57112.pdf","4553346","0.002$/unit0.002$/1 units"],
["CL10A226MQ8NRNC","C59461","B","6.3V","22uF","X5R","±20%","0603","SMD/SMT","ROHS","Samsung Electro-Mechanics","https://datasheet.lcsc.com/lcsc/1811151138_Samsung-Electro-Mechanics-CL10A226MQ8NRNC_C59461.pdf","1482294","0.009$/unit0.009$/1 units"],
["CL10A106MA8NRNC","C96446","B","25V","10uF","X5R","±20%","0603","SMD/SMT","ROHS","Samsung Electro-Mechanics","https://datasheet.lcsc.com/lcsc/1811110921_Samsung-Electro-Mechanics-CL10A106MA8NRNC_C96446.pdf","1261688","0.022$/unit0.022$/1 units"]
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

#0 "CL10A105KB8NNNC"
#1 "C15849"
#2 "B"
#3 "50V"
#4 "1uF"
#5 "X5R"
#6 "±10%"
#7 "0603"
#8 "SMD/SMT"
#9 "ROHS"
#10 "Samsung Electro-Mechanics"
#11 "https://datasheet.lcsc.com/lcsc/1810261812_Samsung-Electro-Mechanics-CL10A105KB8NNNC_C15849.pdf"
#12 "5349163"
#13 "0.005$/unit0.005$/1 units"]


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
