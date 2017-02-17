# threatintel
A sample Splunk App for integrating threat intelligence data into Splunk ES using the Threat Intelligence Framework. This sample app requires that you 
have Splunk ES installed and configured.
It's meant to highlight the process of collecting non-line-oriented data (JSON) and then making that available to the threat intel framework. This is basically two steps

**1. Collect the intel - in this case via a scripted input that writes the JSON data to an Index

**2. Write the IOCs to a lookup - via a saved search that appends indicators to a Splunk lookup - this lookup is then referenced in a theatlist stanza in inputs.conf

Note that if the threat data was in a line-oriented format to begin with (CSV, Tab delimited, etc) - we could go about this in a different manner (no saved search).

##Splunk ES
(from: http://www.splunk.com/en_us/products/premium-solutions/splunk-enterprise-security.html)
Splunk Enterprise Security (ES) is a premium security solution that provides insight into machine data generated from security technologies such as
network, endpoint, access, malware, vulnerability and identity information.

##Threat Intelligence
(from: http://thecyberthreat.com/cyber-threat-intelligence-feeds/)
The discipline of cyber threat intelligence focuses on providing actionable information on adversaries. 
This information is becoming increasingly important to enterprise cyber defense. 
This importance has resulted in investment and creation of many new/innovative sources of information on threat actors

In the context of using threat intelligence to augment security solutions, often the threat intel is boiled down into indicators of some sort; 
domains, ip addresses, file and process hashes, certificates, etc.

##Getting Started
There is an associated document that walks through the Splunk ES Threat Intelligence Framework in depth, of which this example is a companion to. Meaning...if you're reading this, then you have the document already.
The example can be installed similar to any other Splunk App - simply download the files and ensure that the TA-myfirstintel directory is under the
$SPLUNK_HOME/etc/apps directory of your Splunk ES instance.
