# Notes/Reference


### Enable Security Package. 

Requires copy run start/reload after

```
license boot module c2900 technology-package securityk9
```


### Define Crypto ISAKMP Policy

```
    crypto isakmp policy priority attribute_name [attribute_value | integer]
```
You must include the priority in each of the ISAKMP commands. The priority number uniquely identifies the policy,
   and determines the priority of the policy in ISAKMP negotiations.


### Define Crypto Map


```
 crypto map map-name seq-num ipsec-isakmp [dynamic dynamic-map-name]
```

 map-name: The name that identifies the crypto map set. This is the name assigned when the crypto map was created.
 
 seq-num: The number you assign to the crypto map entry.
 
 ipsec-isakmp: Indicates that IKE will be used to establish the IPSec security associations for protecting the traffic specified by this crypto map entry.

 dynamic: (Optional) Specifies that this crypto map entry is to reference a preexisting dynamic crypto map. Dynamic crypto maps are policy templates used in processing negotiation requests from a peer IPSec device. If you use this keyword, none of the crypto map configuration commands will be available.
 
 dynamic-map-name: (Optional) Specifies the name of the dynamic crypto map set that should be used as the policy template.

#### What Crypto Maps Are For

Crypto maps provide two functions: (1) filtering and classifying traffic to be protected and (2) defining the policy to be applied to that traffic. The first use affects the flow of traffic on an interface; the second affects the negotiation performed (via IKE) on behalf of that traffic.

IPSec crypto maps link together definitions of the following:

•What traffic should be protected

•Which IPSec peers the protected traffic can be forwarded to—these are the peers with which a security association can be established

•Which transform sets are acceptable for use with the protected traffic

•How keys and security associations should be used or managed (or what the keys are, if IKE is not used)

#### Multiple Crypto Map Entries with the Same map-name Form a Crypto Map Set

A crypto map set is a collection of crypto map entries, each with a different seq-num but the same map-name. Therefore, for a given interface, you could have certain traffic forwarded to one IPSec peer with specified security applied to that traffic, and other traffic forwarded to the same or a different IPSec peer with different IPSec security applied. To accomplish this you would create two crypto maps, each with the same map-name, but each with a different seq-num.

The seq-num Argument

The number you assign to the seq-num argument should not be arbitrary. This number is used to rank multiple crypto map entries within a crypto map set. Within a crypto map set, a crypto map entry with a lower seq-num is evaluated before a map entry with a higher seq-num; that is, the map entry with the lower number has a higher priority.

For example, imagine that there is a crypto map set that contains three crypto map entries: mymap 10, mymap 20, and mymap 30. The crypto map set named mymap is applied to interface Serial 0. When traffic passes through the Serial 0 interface, the traffic is evaluated first for mymap 10. If the traffic matches a permit entry in the extended access list in mymap 10, the traffic will be processed according to the information defined in mymap 10 (including establishing IPSec security associations when necessary). If the traffic does not match the mymap 10 access list, the traffic will be evaluated for mymap 20, and then mymap 30, until the traffic matches a permit entry in a map entry. (If the traffic does not match a permit entry in any crypto map entry, it will be forwarded without any IPSec security.)

#### Dynamic Crypto Maps

Refer to the "Usage Guidelines" section of the crypto dynamic-map command for a discussion on dynamic crypto maps.

You should make crypto map entries which reference dynamic map sets the lowest priority map entries, so that inbound security association negotiations requests will try to match the static maps first. Only after the request does not match any of the static maps do you want it to be evaluated against the dynamic map set.

To make a crypto map entry referencing a dynamic crypto map set the lowest priority map entry, give the map entry the highest seq-num of all the map entries in a crypto map set.

Create dynamic crypto map entries using the crypto dynamic-map command. After you create a dynamic crypto map set, add the dynamic crypto map set to a static crypto map set with the crypto map (IPSec global configuration) command using the dynamic keyword. 

#### ACLs and NAT Rules

Standard Numbered ACL: 1-99                             Match on Source IP
Extended Numbered ACL: 100-199                          Match on Source and Destination IP/Port
Additional ACL Numbers (1300-1999, 2000-2699 Extended)

ACL gets applied first (before NAT) so if packet is filtered out it never gets NAT translation.
This is why we run commands like:

ip nat inside source list 122 interface GigabitEthernet0/0 overload

    translates the source of IP packets that are traveling inside to outside
    translates the destination of the IP packets that are traveling outside to inside

You can conserve addresses in the inside global address pool by allowing the router to use one global address for many 
local addresses. When this overloading is configured, the router maintains enough information from higher-level protocols 
(for example, TCP or UDP port numbers) to translate the global address back to the correct local address. 
When multiple local addresses map to one global address, the TCP or UDP port numbers of each inside host distinguish 
between the local addresses. 

Overloading--a form of dynamic NAT that maps multiple unregistered IP addresses to a single registered IP address (many to one) 
using different ports. This method is also known as Port Address Translation (PAT). By using PAT (NAT overload), 
thousands of users can be connected to the Internet using only one real global IP address. 

So this command appears to be what tells router not to NAT some traffic but to NAT others, example Router 1 client  ping Router 3 client
no nat and works via VPN. Router 1 client to Router 2 client attempts to NAT (172.16.1.1 is outside address) which fails
because Router 2 is not configured to accept traffic from 172.16.1.1

So router 3 has to accept traffic from both 10.1.1.0 and 10.10.10.0



On Router 1/2:

access-list 1 permit 10.1.1.0 0.0.0.255
access-list 110 permit ip 10.1.1.0 0.0.0.255 10.20.20.0 0.0.0.255
access-list 122 deny ip 10.1.1.0 0.0.0.255 10.20.20.0 0.0.0.255
access-list 122 permit ip 10.1.1.0 0.0.0.255 any



Router 3:

We just need to duplicate this line:

access-list 122 deny ip 10.20.20.0 0.0.0.255 10.1.1.0 0.0.0.255

for router 2?

We end up with:

access-list 1 permit 10.20.20.0 0.0.0.255
access-list 110 permit ip 10.20.20.0 0.0.0.255 10.1.1.0 0.0.0.255
access-list 122 deny ip 10.20.20.0 0.0.0.255 10.1.1.0 0.0.0.255
access-list 122 permit ip 10.20.20.0 0.0.0.255 any
access-list 122 deny ip 10.20.20.0 0.0.0.255 10.10.10.0 0.0.0.255
access-list 120 permit ip 10.20.20.0 0.0.0.255 10.10.10.0 0.0.0.255

Traffic to 10.10.10.10 is still attempting to NAT:

NAT: s=10.20.20.10->10.100.100.2, d=10.10.10.10 [10]

Traffic to router 1 network still not natting, so what is difference?

Perhaps rule order?

Changing order on router 2

Current:

access-list 110 permit ip 10.10.10.0 0.0.0.255 10.20.20.0 0.0.0.255
access-list 122 deny ip 10.10.10.0 0.0.0.255 10.20.20.0 0.0.0.255
access-list 122 permit ip 10.10.10.0 0.0.0.255 any
access-list 1 permit 10.10.10.0 0.0.0.255

Fixed:

access-list 1 permit 10.10.10.0 0.0.0.255
access-list 110 permit ip 10.10.10.0 0.0.0.255 10.20.20.0 0.0.0.255
access-list 122 deny ip 10.10.10.0 0.0.0.255 10.20.20.0 0.0.0.255
access-list 122 permit ip 10.10.10.0 0.0.0.255 any

Order did make a difference, getting isakmp/ipsec debug now

Still not getting through, thinking that the ACL order in Router3 might now be the problem

So for router 3 is this the best configuration?: 

access-list 1 permit 10.20.20.0 0.0.0.255
access-list 110 permit ip 10.20.20.0 0.0.0.255 10.1.1.0 0.0.0.255
access-list 120 permit ip 10.20.20.0 0.0.0.255 10.10.10.0 0.0.0.255
access-list 122 deny ip 10.20.20.0 0.0.0.255 10.1.1.0 0.0.0.255
access-list 122 deny ip 10.20.20.0 0.0.0.255 10.10.10.0 0.0.0.255
access-list 122 permit ip 10.20.20.0 0.0.0.255 any

After putting in that order getting message saying:

%CRYPTO-4-IKMP_NO_SA: IKE message from 10.10.10.10 has no SA and is not an  initialization offer

%CRYPTO-4-RECVD_PKT_INV_SPI: decaps rec'd IPSEC packet has invalid spi for destaddr=10.20.20.10, prot=50, spi=0x22642f0c(576990988), srcaddr=10.10.10.10


Also when showing crypto ipsec SA peer 10.0.0.2 has no outbound esp sas

The fact that it is trying to match on .10 and not .1 makes me think nat is not doing what I want

Message says invalid spi

%CRYPTO-4-RECVD_PKT_INV_SPI: decaps rec'd IPSEC packet has invalid spi for destaddr=10.20.20.10, prot=50, spi=0x22642f0c(576990988), srcaddr=10.10.10.10

Potential options at this point? Different ACL lists

Killing all 122 rules on router 3, I dont understand what they are doing


access-list 122 deny ip 10.20.20.0 0.0.0.255 10.1.1.0 0.0.0.255
access-list 122 deny ip 10.20.20.0 0.0.0.255 10.10.10.0 0.0.0.255
access-list 122 permit ip 10.20.20.0 0.0.0.255 any



Finally got it working with no overload and this ACL setup on R3:


access-list 1 permit 10.20.20.0 0.0.0.255
access-list 110 permit ip 10.20.20.0 0.0.0.255 10.1.1.0 0.0.0.255
access-list 111 permit ip 10.20.20.0 0.0.0.255 10.10.10.0 0.0.0.255
access-list 122 deny ip 10.20.20.0 0.0.0.255 10.1.1.0 0.0.0.255
access-list 122 permit ip 10.20.20.0 0.0.0.255 any
access-list 123 deny ip 10.20.20.0 0.0.0.255 10.10.10.0 0.0.0.255
access-list 123 permit ip 10.20.20.0 0.0.0.255 any