#ifndef TBTDATA_STRUCT_HPP
#define TBTDATA_STRUCT_HPP

// Contains the most commonly used Data Types in the TBT message


#include "Headers.hpp"


//creating everything under FRACTAL namespace
namespace FRACTAL
{
    enum TBTMessageTypes
    {
        ORDER_NEW_TBT_MESSAGE       = 'N',
        ORDER_MODIFY_TBT_MESSAGE    = 'M',
        ORDER_CANCEL_TBT_MESSAGE    = 'X',
        TRADE_TBT_MESSAGE           = 'T',

        SPREAD_ORDER_NEW_TBT_MESSAGE			= 'G',
        SPREAD_ORDER_MODIFY_TBT_MESSAGE			= 'H',
        SPREAD_ORDER_CANCEL_TBT_MESSAGE			= 'J',
        SPREAD_TRADE_TBT_MESSAGE				= 'K'
    };


    enum TBTOrderDirection
    {
        BUY_ORDER       = 'B',
        SELL_ORDER      = 'S'
    };

    struct TBTMessageHeader
    {
        
        int16_t messageSize;
        int streamID;
        int32_t seqNumber;

        char messageType;
    };


    struct TBTOrderMessage
    {
        TBTMessageHeader messageHeader;

        int64_t timestamp;
        int64_t NOT_TO_USE_orderID;
        int64_t orderID;
        int token;
        std::string contractName;
        char direction;
        int32_t price;
        int32_t qty; 

    };


    struct TBTTradeMessage
    {
        TBTMessageHeader messageHeader;

        int64_t timestamp;
        int64_t NOT_TO_USE_orderID;
        int64_t buyOrderID;
        int64_t sellOrderID;
        int token;
        std::string contractName;
        
        int price;
        int qty; 

    };


    union TBTMessage
    {
        TBTOrderMessage tbtOrder;
        TBTTradeMessage tbtTrade;
    };

}

#endif
