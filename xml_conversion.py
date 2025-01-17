xml_content = """<?xml version="1.0" encoding="UTF-8"?>
<ClinicalDocument xmlns="urn:hl7-org:v3" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="urn:hl7-org:v3 CDA.xsd">
  <realmCode code="US"/>
  <typeId root="2.16.840.1.113883.1.3" extension="POCD_HD000040"/>
  <templateId root="2.16.840.1.113883.10.20.22.1.1"/>
  <id root="2.16.840.1.113883.19.5.99999.12345"/>
  <code code="34133-9" codeSystem="2.16.840.1.113883.6.1" codeSystemName="LOINC" displayName="Summary of episode note"/>
  <title>Continuity of Care Document</title>
  <effectiveTime value="2022-01-01"/>
  <confidentialityCode code="N" codeSystem="2.16.840.1.113883.5.25"/>
  <languageCode code="en-US"/>
  <recordTarget>
    <patientRole>
      <id root="2.16.840.1.113883.19.5.99999.12345"/>
      <addr>
        <streetAddressLine>123 Main St</streetAddressLine>
        <city>Anytown</city>
        <state>CA</state>
        <postalCode>12345</postalCode>
      </addr>
      <telecom value="tel:555-555-5555"/>
      <patient>
        <name>
          <given>John</given>
          <family>Doe</family>
        </name>
        <administrativeGenderCode code="M" codeSystem="2.16.840.1.113883.5.1"/>
        <birthTime value="1960-01-01"/>
      </patient>
    </patientRole>
  </recordTarget>
  <component>
    <structuredBody>
      <component>
        <section>
          <templateId root="2.16.840.1.113883.10.20.22.2.3.1"/>
          <code code="11450-4" codeSystem="2.16.840.1.113883.6.1" codeSystemName="LOINC" displayName="Problem List"/>
          <title>Problem List</title>
          <text>
            <list listType="ordered">
              <item>
                <problem>
                  <code code="44054006" codeSystem="2.16.840.1.113883.6.96" codeSystemName="SNOMED-CT" displayName="Onychomycosis"/>
                  <text>Onychomycosis</text>
                  <effectiveTime>
                    <low value="2020-01-01"/>
                  </effectiveTime>
                </problem>
              </item>
              <item>
                <problem>
                  <code code="44054006" codeSystem="2.16.840.1.113883.6.96" codeSystemName="SNOMED-CT" displayName="Type 2 diabetes mellitus"/>
                  <text>Type 2 diabetes mellitus</text>
                  <effectiveTime>
                    <low value="2015-01-01"/>
                  </effectiveTime>
                </problem>
              </item>
              <item>
                <problem>
                  <code code="44054006" codeSystem="2.16.840.1.113883.6.96" codeSystemName="SNOMED-CT" displayName="Microalbuminuric diabetic nephropathy"/>
                  <text>Microalbuminuric diabetic nephropathy</text>
                  <effectiveTime>
                    <low value="2018-01-01"/>
                  </effectiveTime>
                </problem>
              </item>
              <item>
                <problem>
                  <code code="44054006" codeSystem="2.16.840.1.113883.6.96" codeSystemName="SNOMED-CT" displayName="Secondary hyperaldosteronism"/>
                  <text>Secondary hyperaldosteronism</text>
                  <effectiveTime>
                    <low value="2020-06-01"/>
                  </effectiveTime>
                </problem>
              </item>
            </list>
          </text>
        </section>
      </component>
    </structuredBody>
  </component>
</ClinicalDocument>
"""

# Write the XML content to a file
with open("problemlist_output.xml", "w") as file:
    file.write(xml_content)

print("XML file has been created successfully.")
