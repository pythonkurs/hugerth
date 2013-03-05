import untangle
import requests

@profile
def check_outages():
	doc = untangle.parse(requests.get("http://www.grandcentral.org/developers/data/nyct/nyct_ene.xml").content)

	outages=doc.NYCOutages.outage
	total=len(outages)
	repair=0

	for outage in outages:
		if outage.reason.cdata == u'REPAIR':
			repair+=1

	print str(repair) + " / " + str(total)
