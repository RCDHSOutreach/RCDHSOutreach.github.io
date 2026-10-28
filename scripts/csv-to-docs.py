#
# Capstone Import Script
#
# This is a quick and dirty script to convert our checklist CSV to Markdown
#

import csv
import sys

# Global Variables
IMPORT_FILE='checklist.csv'

# Import Mapping - Page Content
pageMap = {
    'GOL': {
        'file': 'goals.md',
        'name': 'Program Goals',
        'items': {}
    },
    'FUN': {
        'file': 'funding.md',
        'name': 'Funding',
        'items': {}
    },
    'STF': {
        'file': 'staffing.md',
        'name': 'Staffing',
        'items': {}
    },
    'TOP': {
        'file': 'topics.md',
        'name': 'Topics for educational activities',
        'items': {}
    },
    'PAR': {
        'file': 'partnerships.md',
        'name': 'Partnerships with campus or industry',
        'items': {}
    },
    'BUY': {
        'file': 'buyin.md',
        'name': 'Buy-in from administration',
        'items': {}
    },
    'LOG': {
        'file': 'logistics.md',
        'name': 'Logistics',
        'items': {}
    },
    'POL': {
        'file': 'policies.md',
        'name': 'Policies',
        'items': {}
    },
    'ACC': {
        'file': 'accessibility.md',
        'name': 'Accessibility and inclusion',
        'items': {}
    },
    'EVL': {
        'file': 'evaluation.md',
        'name': 'Evaluation and impact',
        'items': {}
    },
    'ADV': {
        'file': 'advertising.md',
        'name': 'Advertising and communications',
        'items': {}
    }
}

# Import Mapping - Checklist
programMap = {
    'START_SMALL': {
        'csvIdx': 4,
        'name': 'Start small',
        'file': 'start-small.md',
        'items': []
    },
    'CLASS_PRES': {
        'csvIdx': 5,
        'name': 'Class presentation',
        'file': 'class-presentation.md',
        'items': []
    },
    'WORKSHOP_HALF': {
        'csvIdx': 6,
        'name': 'Half-day workshop',
        'file': 'workshop.md',
        'items': []
    },
    'CAMP_MULTI': {
        'csvIdx': 7,
        'name': 'Multi-day camp (Day Only)',
        'file': 'camp-multi.md',
        'items': []
    },
    'CAMP_MULTI_OVERNIGHT': {
        'csvIdx': 8,
        'name': 'Multi-day camp (Overnight)',
        'file': 'camp-multi-overnight.md',
        'items': []
    }
}

# Generate the page
def generatePage(itemType):
    pageData = pageMap[itemType]

    # Generate the item list in Markdown for page content
    pageItemMD = ''

    # Items - grouped by program type
    for programType in pageData['items']:
        programData = programMap[programType]

        ## Program Type Name
        pageItemMD += '### ' + programData['name'] + '\n'

        ## Collapsible Menu
        pageItemMD += '??? "Checklist Items"\n'

        ## Loop through the items
        for itemData in pageData['items'][programType]:
            pageItemMD += '\t<div class="checklist-item-details" markdown>\n'
            pageItemMD += '\t#### ' + itemData[2] + ' {#' + programType + '_' + itemData[0] + '}\n'
            pageItemMD += '\t**Example**: ' + itemData[3] + '\n'
            pageItemMD += '\t</div>\n'
            pageItemMD += '\t---\n'
            pageItemMD += '\t\n'

        # # Grab information about the program

        # # Section Header
        # pageItemMD += '## ' + itemData[0] + ': ' + itemData[2] + ' {#' + itemData[0] + '} \n'

        # # Program Types
        # programList = []

        # # Which program types were "X" in the spreadsheet
        # for programID in programMap:
        #     if itemData[programMap[programID]['csvIdx']] == 'X':
        #         programList.append(programMap[programID]['name'])

        # pageItemMD += '\n **Programs**: ' + ', '.join(programList) + '\n'

        # # Examples
        # pageItemMD += '\n **Example**: ' + itemData[3] + '\n\n'


    # Open the template file
    tplfp = open('../templates/'+pageData['file'], 'r')

    # Inject the Markdown into the template
    pageFinalMD = tplfp.read().replace('{ITEM_LIST}', pageItemMD)

    # Save the new file
    docfp = open('../docs/'+pageData['file'], 'w')
    docfp.write(pageFinalMD)

    # Close our files
    tplfp.close()
    docfp.close()

# Generate the page
def generatePageOLD(itemType):
    pageData = pageMap[itemType]

    # Generate the item list in Markdown for page content
    pageItemMD = ''

    # Items
    for itemData in pageData['items']:

        # Grab information about the program

        # Section Header
        pageItemMD += '## ' + itemData[0] + ': ' + itemData[2] + ' {#' + itemData[0] + '} \n'

        # Program Types
        programList = []

        # Which program types were "X" in the spreadsheet
        for programID in programMap:
            if itemData[programMap[programID]['csvIdx']] == 'X':
                programList.append(programMap[programID]['name'])

        pageItemMD += '\n **Programs**: ' + ', '.join(programList) + '\n'

        # Examples
        pageItemMD += '\n **Example**: ' + itemData[3] + '\n\n'


    # Open the template file
    tplfp = open('../templates/'+pageData['file'], 'r')

    # Inject the Markdown into the template
    pageFinalMD = tplfp.read().replace('{ITEM_LIST}', pageItemMD)

    # Save the new file
    docfp = open('../docs/'+pageData['file'], 'w')
    docfp.write(pageFinalMD)

    # Close our files
    tplfp.close()
    docfp.close()
    
# Generate Checklist
def generateChecklist():

    # Loop through each program type to build their checklist.
    # - We then replace the variable with our new list.
    for programID in programMap:
        print('Checklist: ' + programID)

        programData = programMap[programID]

        # Open the checklist template for the page
        tplfp = open('../templates/checklists/'+programData['file'], 'r')
        programCLMD = tplfp.read()
        
        curItemType = ''

        # Replace the program name
        programCLMD = programCLMD.replace('{PROGRAM_TYPE}', programData['name'])

        programItemMD = ''

        # Loop through the items
        for item in programData['items']:

            # Which type is this
            itemType = item[0][0:3]
            itemTypeData = pageMap[itemType]

            # Show the section
            if curItemType != itemType:
                programItemMD += '### ' + itemTypeData['name']+'\n'

            # List the item
            programItemMD += '* ' + item[2]+ ' [View Details &raquo;](../' + itemTypeData['file']+'#' + programID + '_' + item[0]+')\n'

            curItemType = itemType

        # Update the template with our new list
        programCLMD = programCLMD.replace('{ITEM_LIST}', programItemMD)

        # Update the program-specific checklist page
        docfp = open('../docs/checklists/'+programData['file'], 'w')
        docfp.write(programCLMD)
        docfp.close()


        # Close the template file
        tplfp.close()

# Read the CSV file
with open(IMPORT_FILE, 'r') as csvFile:
    csvFileData = csv.reader(csvFile)

    # Loop through the rows
    rowIdx = -1

    for row in csvFileData:
        rowIdx = rowIdx + 1

        # Skip the header row
        if rowIdx == 0:
            continue
        
        # Figure out which page this row relates to.
        itemType = row[0][0:3]
        itemName = row[2]

        print(itemType + ' - ' + itemName)

        # Add item to its section
        # pageMap[itemType]['items'].append(row)

        # Add the item to its program.
        for programID in programMap:
            if row[programMap[programID]['csvIdx']] == 'X':

                # Tie to the program (grouped by program)
                programMap[programID]['items'].append(row)

                # Tie to the program (grouped by category)
                if programID not in pageMap[itemType]['items']:
                    pageMap[itemType]['items'][programID] = []
    
                pageMap[itemType]['items'][programID].append(row)
                

        

    # Generate our pages
    for pageType in pageMap:
        print('Generating ' + pageType)
        generatePage(pageType)

    # Generate our checklist
    print('Generating checklists')
    generateChecklist()