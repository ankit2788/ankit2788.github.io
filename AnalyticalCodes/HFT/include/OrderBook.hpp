#ifndef ORDERBOOK_HPP
#define ORDERBOOK_HPP

#include <TBTDataStructure.hpp>
#include "OrderBookDataStructure.hpp"

namespace FRACTAL
{

    #define INVALID_PRICE   -1

    class OrderBook
    {
        private:

            OrderBook(const OrderBook&);        //disable copy constructor and assignment constructor
            OrderBook& operator = (const OrderBook&);       //disable default assignment operator

            void getPriceTimePriority(TBTOrderDirection direction, int32_t price, int32_t seqNumber, int64_t& priceTimePriority /*out*/ );

            //Basic operations required on the OrderBook
            void insertOrder(OrderBook &orderbook, TBTOrderMessage &tbtOrdermessage);
            void modifyOrder(OrderBook &orderbook, TBTOrderMessage &tbtOrdermessage);
            void deleteOrder(OrderBook &orderbook, TBTOrderMessage &tbtOrdermessage);
            void searchOrder(OrderBook &orderbook, TBTOrderMessage &tbtOrdermessage);

            OrderBookContainer bidOrderBookContainer;
            OrderBookContainer askOrderBookContainer;

            
            int bestBidPrice;
            int bestAskPrice;
            int lastTradedPrice;



        public:
            OrderBook();        //empty constructor

            //TODO: check whether to use pass by reference or pass by pointer
            void processTBTMessage(OrderBook &orderbook, TBTMessage &tbtmessage);   //processes TBT message as receievd

            int getBestBidPrice();
            int getBestAskPrice();
            int getMidPrice();
            int getLastTradedPrice();

    };



}


#endif