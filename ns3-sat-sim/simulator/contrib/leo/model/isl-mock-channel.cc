/* -*- Mode:C++; c-file-style:"gnu"; indent-tabs-mode:nil; -*- */
/*
 * Copyright (c) 2007, 2008 University of Washington
 *
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License version 2 as
 * published by the Free Software Foundation;
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
 */

#include <ns3/trace-source-accessor.h>
#include <ns3/packet.h>
#include <ns3/simulator.h>
#include <ns3/log.h>
#include <ns3/pointer.h>
#include "isl-mock-channel.h"



namespace ns3 {

NS_LOG_COMPONENT_DEFINE ("IslMockChannel");

NS_OBJECT_ENSURE_REGISTERED (IslMockChannel);

TypeId
IslMockChannel::GetTypeId (void)
{
  static TypeId tid = TypeId ("ns3::IslMockChannel")
    .SetParent<MockChannel> ()
    .SetGroupName ("Leo")
    .AddConstructor<IslMockChannel> ()
  //SPE-modification
  .AddAttribute("nOrbits",
                "Number of orbits", 
                IntegerValue(27),
                MakeIntegerAccessor(&IslMockChannel::m_nOrbits),
                MakeIntegerChecker<int>())
  .AddAttribute("nSatsPerOrbit", "Number of satellites per orbit", 
                IntegerValue(27),
                MakeIntegerAccessor(&IslMockChannel::m_nSatsPerOrbit),
                MakeIntegerChecker<int>())
  ;
  return tid;
}

//
// By default, you get a channel that
// has an "infitely" fast transmission speed and zero processing delay.
IslMockChannel::IslMockChannel() : MockChannel ()
{
  NS_LOG_FUNCTION_NOARGS ();
}

IslMockChannel::~IslMockChannel()
{
}

bool
IslMockChannel::TransmitStart (
    Ptr<const Packet> p,
    uint32_t srcId,
    Address destAddr,
    Time txTime)
{
  NS_LOG_FUNCTION (this << p << srcId << destAddr << txTime);
  NS_LOG_LOGIC ("UID is " << p->GetUid () << ")");

  if (srcId >= GetNDevices ())
    {
      NS_LOG_ERROR ("Source device unknown");
      return false;
    }
  Ptr<MockNetDevice> src = StaticCast<MockNetDevice> (GetDevice (srcId));
  Ptr<MockNetDevice> dst = StaticCast<MockNetDevice> (GetDevice (destAddr));

//SPE-modification
/*
  if (dst == nullptr)
  {
    if (Mac48Address::ConvertFrom (destAddr).IsBroadcast () || Mac48Address::ConvertFrom (destAddr).IsBroadcast ())
      // try to deliver to every node in LOS
      {
        for (size_t i = 0; i < GetNDevices (); i ++)
          {
	    NS_LOG_DEBUG ("i "<<i<<" device "<<GetDevice(i));
            if (i == srcId) continue;
            dst = StaticCast<MockNetDevice> (GetDevice (i));
            Deliver (p, src, dst, txTime);
          }
        return true;
      }
    else
      {
        NS_LOG_ERROR ("destination address " << destAddr << " unknown on channel");
        return false;
      }
  }
  else
  {
    return Deliver (p, src, dst, txTime);
  }
*/


  if (dst == nullptr)
  {
	if (Mac48Address::ConvertFrom (destAddr).IsBroadcast()||Mac48Address::ConvertFrom (destAddr).IsBroadcast())
	  {

                //SPE-modification: to implement +grid topology
		/*
		uint32_t orbits=34; //34 for Kuiper K1 - 27 for Telesat T1 - 72 for Starlink S1;
		uint32_t sat_per_orbit=34; //34 for Kuiper K1 - 13 for Telesat T1 - 22 for Starlink S1;
		uint32_t next=(srcId+1)%sat_per_orbit+sat_per_orbit*(srcId/sat_per_orbit);
		uint32_t previous=(srcId-1)%sat_per_orbit+sat_per_orbit*(srcId/sat_per_orbit);
		uint32_t prev_orbit=(srcId-sat_per_orbit)%(sat_per_orbit*orbits);
		uint32_t next_orbit=(srcId+sat_per_orbit)%(sat_per_orbit*orbits);
		*/

		uint32_t next=(srcId+1)%m_nSatsPerOrbit+m_nSatsPerOrbit*(srcId/m_nSatsPerOrbit);
		uint32_t previous=(srcId-1)%m_nSatsPerOrbit+m_nSatsPerOrbit*(srcId/m_nSatsPerOrbit);
		uint32_t prev_orbit=(srcId-m_nSatsPerOrbit)%(m_nSatsPerOrbit*m_nOrbits);
		uint32_t next_orbit=(srcId+m_nSatsPerOrbit)%(m_nSatsPerOrbit*m_nOrbits);


		NS_LOG_DEBUG("");
		NS_LOG_DEBUG("src "<< srcId << " next_in_orbit " << next << " previous_in_orbit " << previous << " sat_in_prev_orbit "<< prev_orbit << " sat_in_next_orbit " << next_orbit);
		NS_LOG_DEBUG("");

		dst=StaticCast<MockNetDevice> (GetDevice(next)); 
		Deliver (p,src,dst,txTime);

		dst=StaticCast<MockNetDevice> (GetDevice(previous)); 
		Deliver (p,src,dst,txTime);
 
		dst=StaticCast<MockNetDevice> (GetDevice(prev_orbit)); 
		Deliver (p,src,dst,txTime);
 
		dst=StaticCast<MockNetDevice> (GetDevice(next_orbit)); 
		Deliver (p,src,dst,txTime);

		return true;

          }
	else
	  {
		NS_LOG_ERROR("destination address " << destAddr << "unknown on channel");
		return false;
	  }

  }
  else
  {
	return Deliver(p,src,dst,txTime);
  }


}

} // namespace ns3
