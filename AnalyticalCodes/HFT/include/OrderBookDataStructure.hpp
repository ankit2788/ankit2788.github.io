#ifndef ORDERBOOK_DATASTRUCT_HPP
#define ORDERBOOK_DATASTRUCT_HPP

#include "Headers.hpp"

#include <boost/multi_index_container.hpp>
#include <boost/multi_index/member.hpp>
#include <boost/multi_index/ordered_index.hpp>
#include <boost/multi_index/hashed_index.hpp>

namespace FRACTAL
{
    enum OrderBookTypes
    {
        BuySideBook,
        SellSideBook
    };

    struct OrderBookStructure
    {
        bool isOwn;
        int price;
        int qty;
        //int nbOrders;

        int64_t OrderID;
        int64_t timestamp;      //for price time priority
        int64_t pricetimepriority;


    };

    /*
    Creating a multi index data structure for the OrderBook, for easy entry, lookup and deletion.
    1. Hashed Index created on OrderID (1st level)
    2. Ordered Index created on Timestamp
    */


    struct OrderByExchOrderIdHashIndexTag{};
    struct OrderByPriceTimePriorityOrderedIndexTag{};


    typedef boost::multi_index::multi_index_container < 
        OrderBookStructure,
        boost::multi_index::indexed_by<
            boost::multi_index::hashed_unique<
                boost::multi_index::tag<OrderByExchOrderIdHashIndexTag>, 
                boost::multi_index::member<OrderBookStructure, int64_t, &OrderBookStructure::OrderID>
                >,
            boost::multi_index::ordered_unique<
                boost::multi_index::tag<OrderByPriceTimePriorityOrderedIndexTag>,
                boost::multi_index::member<OrderBookStructure, int16_t, &OrderBookStructure::pricetimepriority>
            >
        > 
    >OrderBookContainer;
     


    typedef OrderBookContainer::index<OrderByExchOrderIdHashIndexTag>::type OrderByExchOrderIdHashIndex;
    typedef OrderBookContainer::index<OrderByPriceTimePriorityOrderedIndexTag>::type OrderByPriceTimePriorityOrderedIndex;




}//FRACTAL

#endif  //ORDERBOOK_DATASTRUCT_HPP

