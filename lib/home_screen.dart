import 'services/coins_service.dart';

class HomeScreen {
  final CoinsService _coinsService = CoinsService();

  void demo() {
    _coinsService.addCoins(10);
    _coinsService.spendCoins(3);
    print('Coins left: ${_coinsService.coins}');
  }
}
