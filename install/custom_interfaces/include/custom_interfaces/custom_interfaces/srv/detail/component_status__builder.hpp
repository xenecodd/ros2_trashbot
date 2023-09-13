// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from custom_interfaces:srv/ComponentStatus.idl
// generated code does not contain a copyright notice

#ifndef CUSTOM_INTERFACES__SRV__DETAIL__COMPONENT_STATUS__BUILDER_HPP_
#define CUSTOM_INTERFACES__SRV__DETAIL__COMPONENT_STATUS__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "custom_interfaces/srv/detail/component_status__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace custom_interfaces
{

namespace srv
{

namespace builder
{

class Init_ComponentStatus_Request_component
{
public:
  Init_ComponentStatus_Request_component()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::custom_interfaces::srv::ComponentStatus_Request component(::custom_interfaces::srv::ComponentStatus_Request::_component_type arg)
  {
    msg_.component = std::move(arg);
    return std::move(msg_);
  }

private:
  ::custom_interfaces::srv::ComponentStatus_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::custom_interfaces::srv::ComponentStatus_Request>()
{
  return custom_interfaces::srv::builder::Init_ComponentStatus_Request_component();
}

}  // namespace custom_interfaces


namespace custom_interfaces
{

namespace srv
{

namespace builder
{

class Init_ComponentStatus_Response_status
{
public:
  Init_ComponentStatus_Response_status()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::custom_interfaces::srv::ComponentStatus_Response status(::custom_interfaces::srv::ComponentStatus_Response::_status_type arg)
  {
    msg_.status = std::move(arg);
    return std::move(msg_);
  }

private:
  ::custom_interfaces::srv::ComponentStatus_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::custom_interfaces::srv::ComponentStatus_Response>()
{
  return custom_interfaces::srv::builder::Init_ComponentStatus_Response_status();
}

}  // namespace custom_interfaces

#endif  // CUSTOM_INTERFACES__SRV__DETAIL__COMPONENT_STATUS__BUILDER_HPP_
