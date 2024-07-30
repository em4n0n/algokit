from algopy import *


class DigitalMarketplace(ARC4Contract):
    assetId: UInt64
    unitaryPrice = UInt64
    # create the application
    @arc4.abimethod(allow_ations=["NoOp"], create="require")
    def createApplication(self, assetID, unitaryPrice: UInt64) -> None:
        self.assetId = assetID
        self.unitaryPrice = unitaryPrice
    
    # update the listing price
    @arc4.abimethod
    def setPrice(self, unitaryPrice: UInt64): -> None:
        assert Txn.sender == Global.creator_address
        self.unitaryPrice = unitaryPrice


    # opt in to the asset that will be sold
    @arc4_abimethod
    def optInToAsset(self, mbrPay: gtxn.PaymentTransaction) -> None:
        
    # buy the asset

    # delete the application
