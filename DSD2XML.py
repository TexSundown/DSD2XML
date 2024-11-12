import sys

def main():
    # Check if the correct number of arguments are provided
    if len(sys.argv) != 3:
        print("Usage: python DSD2XML.py [DSD .radio file] [XML Output file]")
        sys.exit(1)
    
    try:
        dsd = open(sys.argv[1])
        xmlInput = ""
        
    except:
        print("DSD file does not exist")
    
    for line in dsd:
        lineVals = line.split(",")
        lineVals[8] = lineVals[8].replace('"','').replace(" ","").replace('\n',"").replace('*','')
        xmlInput += f'''
<alias name="{lineVals[8]}" color="-65281" group="RADIOS" list="DART" iconName="Bus">
    <id type="radio" value="{lineVals[3].replace(' ', '')}" protocol="APCO25"/>
    <id type="priority" priority="-1"/>
</alias>'''
    try:
        xml = open(sys.argv[2], "w")
        xml.write(xmlInput)
    except:
        print("Output file directory does not exist/Improper permissions to edit output file")


if __name__ == "__main__":
    main()
