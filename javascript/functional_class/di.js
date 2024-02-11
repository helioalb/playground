function userRepository() {
  return {
    findById: function(id) {
      if (id === 1)
        return 'John Doe';
    }
  }
}

function orderRepository() {
  return {
    itemsByOrderId: function(orderId) {
      if (orderId === 123)
        return ['product x', 'product y'];
    }
  }
}

function reportService({ userRepository, orderRepository }) {
  return {
    createReport: function (userId, orderId) {
      const userName = userRepository.findById(userId);
      const items = orderRepository.itemsByOrderId(orderId);
      return `${userName} bought: ${items}`;
    }
  }
}

const svc = reportService({
  userRepository: userRepository(),
  orderRepository: orderRepository()
});

const report = svc.createReport(1, 123);
console.log(report);
