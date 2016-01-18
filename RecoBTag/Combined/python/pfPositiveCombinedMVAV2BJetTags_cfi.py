import FWCore.ParameterSet.Config as cms

pfPositiveCombinedMVAV2BJetTags = cms.EDProducer("JetTagProducer",
	jetTagComputer = cms.string('candidatePositiveCombinedMVAV2Computer'),
	tagInfos = cms.VInputTag(
		cms.InputTag("pfImpactParameterTagInfos"),
		cms.InputTag("pfSecondaryVertexPositiveTagInfos"),
		cms.InputTag("pfInclusiveSecondaryVertexFinderPositiveTagInfos"),
		cms.InputTag("softPFMuonsTagInfos"),
		cms.InputTag("softPFElectronsTagInfos")
	)
)
