# threatintel
A sample Splunk App for integrating threat intelligence data into Splunk ES using the Threat Intelligence Framework. This sample app requires that you 
have Splunk ES installed and configured.

##Splunk ES
(from: http://www.splunk.com/en_us/products/premium-solutions/splunk-enterprise-security.html)
Splunk Enterprise Security (ES) is a premium security solution that provides insight into machine data generated from security technologies such as
network, endpoint, access, malware, vulnerability and identity information.

##Threat Intelligence
(from: http://thecyberthreat.com/cyber-threat-intelligence-feeds/)
The discipline of cyber threat intelligence focuses on providing actionable information on adversaries. 
This information is becoming increasingly important to enterprise cyber defense. 
This importance has resulted in investment and creation of many new/innovative sources of information on threat actors

In the context of using threat intelligence to augment security solutions, often the threat intel is boiled down into indictors of some sort; 
domains, ip addresses, file and process hashes, certificates, etc.

##Getting Started
There is an associated document that walks through the Splunk ES Threat Intelligence Framework in depth, of which this example is a companion to.
The example can be installed similar to any other Splunk App - simply download the files and ensure that the TA-myfirstintel directory is under the
$SPLUNK_HOME/etc/apps directory of your Splunk ES instance.
