var events = {
	'11-21-2019' : [{content: 'Great American Smokeout', url: 'http://www.wincalendar.com/Great-American-Smokeout', allDay: true}],
	'11-13-2019' : [{content: 'Ashura [An example of an complete date event (11-13-2019)]', allDay: true}],
	'11-11-2019' : [{content: 'Remembrance Day (Canada)', url: 'http://www.wincalendar.com/Remembrance-Day', allDay: true}], 
	'11-04-2019' : [{content: 'Islamic New Year', repeat: 'YEARLY', allDay: true, endDate: '12-31-2019'}],
	'12-25-2019' : [{content: 'Christmas Day', repeat: 'YEARLY', allDay: true, endDate: '12-31-2019'}],
	'01-01-2019' : [{content: 'New Year\'s', repeat: 'YEARLY', allDay: true, endDate: '12-31-2019'}],
	'03-02-2019' : [{content: 'Yeah Monthly', repeat: 'MONTHLY', allDay: true, endDate: '07-02-2019'}],
	'01-07-2019' : [{content: 'Monthly And Yearly', repeat: 'MONTHLY', allDay: true, endDate: '02-07-2019'}],
	'03-02-2019' : [{content : 'Graduation Exams', repeat: 'INTERVAL', allDay: true, endDate: '03-20-2019'}],
	'04-01-2019' : [{content : 'MONDAY (WEEKLY)', repeat: 'MON', allDay: true, endDate: '04-30-2019'}]
},
t = new Date(),
//Creation of today event
today = ((t.getMonth() + 1) < 10 ? '0' + (t.getMonth() + 1) : (t.getMonth() + 1)) + '-' + (t.getDate() < 10 ? '0' + t.getDate() : t.getDate()) + '-' +t.getFullYear();
events[today] = [{content: 'TODAY', allDay: true, endDate: '05-16-2019'},{content: 'apple', allDay: true, endDate: '05-16-2019'}];
