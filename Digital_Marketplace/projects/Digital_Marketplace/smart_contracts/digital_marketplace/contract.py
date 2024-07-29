from algopy import ARC4Contract, String
from algopy.arc4 import abimethod


class DigitalMarketplace(ARC4Contract):
    assetId: UInt64
    unitaryPrice = UInt64
    # create the application
    @arc4. abimethod(allow_ations=["NoOp"], create="require")
    def createApplication(self, assetID, unitaryPrice: UInt64) -> None:
        self.assetId = assetID
        self.unitaryPrice = unitaryPrice
    
    # update the listing price

    # opt in to the asset that will be sold

    # buy the asset

    # delete the application
