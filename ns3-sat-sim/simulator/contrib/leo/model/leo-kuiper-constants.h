/* -*- Mode:C++; c-file-style:"gnu"; indent-tabs-mode:nil; -*- */
/*
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
 *
 * Author: Tim Schubert <ns-3-leo@timschubert.net>
 */

#ifndef LEO_KUIPER_CONSTANTS
#define LEO_KUIPER_CONSTANTS

/**
 * \file
 * \ingroup leo
 * Definition of Kuiper link constants
 */

namespace ns3 {

/**
 * \ingroup leo
 * \brief Constants for starlink network estimated from channel parameters
 *
 * Source http://systemarchitect.mit.edu/docs/delportillo18b.pdf
 *
 */

// gateway uplink
#define LEO_KUIPER_GATEWAY_FREQUENCY        28.5           // GHz
#define LEO_KUIPER_GATEWAY_BANDWIDTH        0.5            // GHz
#define LEO_KUIPER_GATEWAY_TX_ANTENNA_D     3.5            // m
#define LEO_KUIPER_GATEWAY_EIRP             92.3           // dBm
#define LEO_KUIPER_GATEWAY_MODCOD           "256APSK 3/4"  // -
#define LEO_KUIPER_GATEWAY_ROLL_OFF_FACTOR  0.1            // -
#define LEO_KUIPER_GATEWAY_SPECTRAL_EFF     5.4            // bps/Hz
#define LEO_KUIPER_GATEWAY_PATH_DISTANCE    1012.5           // 1124.10 - 1012.50km
#define LEO_KUIPER_GATEWAY_ELEVATION_ANGLE  35             // 30-35deg
#define LEO_KUIPER_GATEWAY_FSPL             181.644          // 182.553058 - 181.644822 dB
#define LEO_KUIPER_GATEWAY_ATMOSPHERIC_LOSS 2.9            // (no lo cambio de Starlink, xq no he encontrado formula) dB
#define LEO_KUIPER_GATEWAY_RX_ANTENNA_GAIN  40.9           // dBi
#define LEO_KUIPER_GATEWAY_SYSTEM_TEMP      535.9          // K
#define LEO_KUIPER_GATEWAY_G_T              13.6           // dB/K
#define LEO_KUIPER_GATEWAY_RX_C_N0          32.4           // dB
#define LEO_KUIPER_GATEWAY_RX_C_ACI         27             // dB
#define LEO_KUIPER_GATEWAY_RX_C_ASI         27             // dB
#define LEO_KUIPER_GATEWAY_RX_C_XPI         25             // dB
#define LEO_KUIPER_GATEWAY_HPA_C_3IM        30             // dB
#define LEO_KUIPER_GATEWAY_RX_EB_N0_I0      13.3           // dB
#define LEO_KUIPER_GATEWAY_REQ_EB_N0        12.3           // dB
#define LEO_KUIPER_GATEWAY_LINK_MARGIN      1.02           // (no lo cambio porque no he encontrado fórmula) dB
//#define LEO_KUIPER_GATEWAY_DATA_RATE        "2682.1Mbps"         // Mbps
#define LEO_KUIPER_GATEWAY_DATA_RATE        "10Mbps"         // Mbps
#define LEO_KUIPER_GATEWAY_SHANNON_LIMIT    1.06           // dB

// user uplink
#define LEO_KUIPER_USER_FREQUENCY           13.5           // GHz
#define LEO_KUIPER_USER_BANDWIDTH           0.25           // GHz
#define LEO_KUIPER_USER_EIRP                66.7           // dBm
#define LEO_KUIPER_USER_MODCOD              "16APSK3/4"    // -
#define LEO_KUIPER_USER_ROLL_OFF_FACTOR     0.1            // -
#define LEO_KUIPER_USER_SPECTRAL_EFF        2.7            // bps/Hz
#define LEO_KUIPER_USER_PATH_DISTANCE       1684           // km
//#define LEO_KUIPER_USER_ELEVATION_ANGLE     40             // deg
#define LEO_KUIPER_USER_ELEVATION_ANGLE     35             // deg
#define LEO_KUIPER_USER_FSPL                179.6          // dB
#define LEO_KUIPER_USER_ATMOSPHERIC_LOSS    0.53           // dB
#define LEO_KUIPER_GATEWAY_RX_ANTENNA_D     0.7            // m
#define LEO_KUIPER_USER_RX_ANTENNA_GAIN     37.7           // dBi
#define LEO_KUIPER_USER_SYSTEM_TEMP         362.9          // K
#define LEO_KUIPER_USER_RX_C_N0             12.0           // dB
#define LEO_KUIPER_USER_RX_C_ASI            25             // dB
#define LEO_KUIPER_USER_RX_C_XPI            22             // dB
#define LEO_KUIPER_USER_HPA_C_3IM           25             // dB
#define LEO_KUIPER_USER_RX_EB_N0_I0         6.7            // dB
#define LEO_KUIPER_USER_REQ_EB_N0           5.9            // dB
#define LEO_KUIPER_USER_LINK_MARGIN         0.82           // dB
//#define LEO_KUIPER_USER_DATA_RATE           "674.3Mbps"          // Mbps
#define LEO_KUIPER_USER_DATA_RATE           "10Mbps"          // Mbps
#define LEO_KUIPER_USER_SHANNON_LIMIT       1.46           // dB

};

#endif
