

#include <iostream>
#include "OrderBook.hpp"

namespace FRACTAL
{

    //Initializing Orderbook with dummy values
    OrderBook::OrderBook():
        bestBidPrice(INVALID_PRICE),
        bestAskPrice(INVALID_PRICE),
        lastTradedPrice(INVALID_PRICE)
        {}


    //Function to return the priceTime priority
    void OrderBook::getPriceTimePriority(TBTOrderDirection direction, int32_t price, int32_t seqNumber, int64_t& priceTimePriority /*out*/ )
    {
        /*
        TBT message contains sequence number of every message. Using that, and price mentioned in the tick, we determine the price time priority. 
        */
        priceTimePriority = ((int64_t)(direction == BUY_ORDER ? -price : price) << 32) + seqNumber;	// Lower is better.
    }



    //Function to insert a new tick into the existing orderbook
    void OrderBook::insertOrder(OrderBook &orderbook, TBTOrderMessage &tbtOrdermessage)
    {

        assert (tbtOrdermessage.messageHeader.messageType ==  ORDER_NEW_TBT_MESSAGE);

        /*
        1. If Orderbook empty, insert the new tick at the top
        2. If price of new tick message is same as one of the existing levels, then insert at the last of that price level
        3. If price is not present, then insert another level for this tick message
        */

        //sanity checks
        if (tbtOrdermessage.price <=0 || tbtOrdermessage.qty <=0)
        {
            throw ("Either price or qty is negative. Mission Abort!");
        }

        //Prepare for the OrderBook entry
        OrderBookStructure newOrder;
        newOrder.price = tbtOrdermessage.price;
        newOrder.qty = tbtOrdermessage.qty;
        newOrder.timestamp = tbtOrdermessage.timestamp;
        newOrder.OrderID = tbtOrdermessage.orderID;
        

        //get the priceTime priority of this new order
        getPriceTimePriority((TBTOrderDirection)tbtOrdermessage.direction, newOrder.price, tbtOrdermessage.messageHeader.seqNumber, newOrder.pricetimepriority);


        //Inserting new order into the orderbook
        OrderByPriceTimePriorityOrderedIndex& orderedIndex = 

		OrderByPriceTimePriorityOrderedIndex& orderedIndex = (tbtOrderMsg->orderType == BUY_ORDER_TBT ? buyOrderBookContainer_ : sellOrderBookContainer_).get<OrderByPriceTimePriorityOrderedIndexTag>();
		std::pair<OrderByPriceTimePriorityOrderedIndex::iterator, bool> insertReturn = orderedIndex.insert(orderBookEntry);

		if(!insertReturn.second)
			throw std::string("Error: ContractBook::processTbtMessage(): case ORDER_NEW_TBT_MESSAGE: insert() to order book failed. ExchOrderId: ")
				+ boost::lexical_cast<std::string>(orderBookEntry.exchOrderId);




    }


    
    

}//FRACTAL