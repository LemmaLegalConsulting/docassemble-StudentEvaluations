from docassemble.base.core import DAObject, DAList, DADict

__all__ = ['PRSTranslatedDocuments', 'PRSMeetings', 'PRSIndividualDocument', 'PRSIndividualMeeting']

class PRSIndividualDocument(DAObject):
    def init(self, *pargs, **kwargs):
        super(PRSIndividualDocument, self).init(*pargs, **kwargs) # Run the parent DAList class constructor before we do our own initialization
        self.complete_attribute = 'prs_document_complete'
    
    @property
    def prs_document_complete(self):
        self.name
        self.type
        self.date

class PRSRequestInformation(DAObject):
    def init(self, *pargs, **kwargs):
        super(PRSRequestInformation, self).init(*pargs, **kwargs) # Run the parent DAList class constructor before we do our own initialization
        self.complete_attribute = 'prs_request_information_complete'
    
    @property
    def prs_request_information_complete(self):
        self.requested_from
        self.how_requested
        self.date_requested
        self.documentation_attached

class PRSIndividualMeeting(DAObject):
    def init(self, *pargs, **kwargs):
        super(PRSIndividualMeeting, self).init(*pargs, **kwargs) # Run the parent DAList class constructor before we do our own initialization
        self.complete_attribute = 'prs_meeting_complete'
        self.initializeAttribute('prs_request_information', PRSRequestInformation)
    
    @property
    def prs_meeting_complete(self):
        self.name
        self.date
        self.requested
        self.any_interpretation

class PRSTranslatedDocuments(DAList):
    def init(self, *pargs, **kwargs):
        super(PRSTranslatedDocuments, self).init(*pargs, **kwargs) # Run the parent DAList class constructor before we do our own initialization
        self.object_type = PRSIndividualDocument

class PRSMeetings(DAList):
    def init(self, *pargs, **kwargs):
        super(PRSMeetings, self).init(*pargs, **kwargs)
        self.object_type = PRSIndividualMeeting
